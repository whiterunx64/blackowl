import os
import shlex
import shutil
import subprocess
import getpass

class Installer:
    """
    Handles interactions with pacman, repository setup, wrapper creation,
    and menu (.desktop) generation.
    """
    def __init__(self, system):
        self.system = system
        self.console = system.console

    # === PACMAN HELPERS ===
    def pacman_group_tools(self, group: str):
        try:
            result = subprocess.run(
                f"pacman -Sg {group}",
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True
            )
            tools = set()
            for line in result.stdout.strip().splitlines():
                parts = line.split()
                if len(parts) == 2:
                    tools.add(parts[1])
            return sorted(tools)
        except subprocess.CalledProcessError:
            return []

    def pacman_installed(self, tool: str) -> bool:
        result = subprocess.run(
            f"pacman -Q {tool}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0

    def pacman_install(self, tool: str):
        self.console.print(f"[yellow]Installing [bold]{tool}[/bold] ...[/yellow]")
        self.system.run_command(f"sudo pacman -S --noconfirm {tool}")

    # === WRAPPER & DESKTOP ENTRY ===
    def create_wrapper(self, tool: str):
        wrapper_path = f"/usr/bin/{tool}-helper"
        help_text = ""

        for cmd in [
            f"{shlex.quote(tool)} --help",
            f"{shlex.quote(tool)} -h",
            f"{shlex.quote(tool)} -H",
            f"{shlex.quote(tool)} -HH",
            f"man {shlex.quote(tool)}"
        ]:
            try:
                result = subprocess.run(
                    cmd,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    timeout=5
                )
                if result.stdout and "not found" not in result.stdout.lower():
                    filtered = "\n".join(
                        line for line in result.stdout.strip().splitlines()
                        if "illegal option" not in line.lower() and "does not exist" not in line.lower()
                    )
                    if filtered.strip():
                        help_text = filtered
                        break
            except Exception:
                continue

        if not help_text:
            help_text = f"No help available for {tool}."

        content = f"""#!/bin/zsh
if [ "$#" -eq 0 ] || [[ "$1" == "--help" || "$1" == "-h" || "$1" == "-H" || "$1" == "-HH" ]]; then
cat <<'EOF'
{help_text}
EOF
exit 0
fi
{tool} "$@"
echo
echo "Press Enter to close this window..."
read
"""
        # write file as root
        proc = subprocess.Popen(['sudo', 'tee', wrapper_path], stdin=subprocess.PIPE)
        proc.communicate(input=content.encode())
        self.system.run_command(f"sudo chmod +x {wrapper_path}")

    def batch_install_and_create_wrappers(self, tools):
        for tool in tools:
            if not self.pacman_installed(tool):
                self.console.print(f"[yellow]Installing [bold]{tool}[/bold] ...[/yellow]")
                result = subprocess.run(f"sudo pacman -S --noconfirm {tool}", shell=True)
                if result.returncode != 0:
                    self.console.print(f"[red]Error: target not found: {tool}[/red]")
                    continue
            self.create_wrapper(tool)

    # === REPO & MENUS ===
    def update_repo(self):
        self.console.print("[bold yellow]Updating system package database...[/bold yellow]")
        self.system.run_command("sudo pacman -Syy --noconfirm")
        self.console.print("[green]Update complete.[/green]")

    def install_blackarch_repo(self):
        self.console.print("[bold yellow]Installing BlackArch repository...[/bold yellow]")
        self.system.run_command("curl -O https://blackarch.org/strap.sh")
        sha_check = subprocess.run(
            "echo bbf0a0b838aed0ec05fff2d375dd17591cbdf8aa strap.sh | sha1sum -c",
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if "OK" not in sha_check.stdout:
            self.console.print("[red]SHA1 verification failed! Aborting.[/red]")
            return
        self.system.run_command("chmod +x strap.sh")
        self.system.run_command("sudo ./strap.sh")
        self.console.print("[yellow]Please enable multilib in /etc/pacman.conf if you haven't already.[/yellow]")
        self.console.print("[yellow]See: https://wiki.archlinux.org/index.php/Official_repositories#Enabling_multilib[/yellow]")
        input("Press Enter to continue to full system update...")
        self.system.run_command("sudo pacman -Syu")
        self.console.print("[green]BlackArch repository installation complete![/green]")
        input("Press Enter to continue...")

    def generate_blackarch_menus(self, groups_dict):
        user = getpass.getuser()
        menu_dir = os.path.expanduser(f"~{user}/.local/share/applications/BlackArch")
        os.makedirs(menu_dir, exist_ok=True)
        result = subprocess.run("pacman -Qqg | grep '^blackarch-'", shell=True, stdout=subprocess.PIPE, text=True)
        tool_groups = {}
        for line in result.stdout.strip().splitlines():
            group, tool = line.split()
            tool_groups.setdefault(group, []).append(tool)
        for group, tools in tool_groups.items():
            group_name = groups_dict.get(group, (group, ""))[0]
            for tool in tools:
                tool_path = shutil.which(tool)
                if not tool_path:
                    continue
                desktop_path = os.path.join(menu_dir, f"{tool}.desktop")
                desktop_content = f"""[Desktop Entry]
Type=Application
Name={tool} ({group_name})
Exec={tool}
Icon=utilities-terminal
Terminal=true
Categories=BlackArch;{group};
"""
                with open(desktop_path, "w") as f:
                    f.write(desktop_content)
                os.chmod(desktop_path, 0o755)
        print(f"BlackArch menus generated in {menu_dir}")
