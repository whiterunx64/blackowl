import sys

class MenuManager:
    """
    Handles all interactive menus and user choices.
    """
    def __init__(self, system, data, installer):
        self.system = system
        self.console = system.console
        self.data = data
        self.installer = installer

    # === MENUS ===
    def tool_menu(self, group_key: str, tools):
        while True:
            self.system.clear_screen()
            spacing, columns = 22, 4
            rows = (len(tools) + columns - 1) // columns
            lines = []
            for r in range(rows):
                line = []
                for c in range(columns):
                    idx = r + c * rows
                    if idx < len(tools):
                        opt_str = f"{idx+1}. {tools[idx]}"
                        line.append(opt_str.ljust(spacing))
                lines.append("  ".join(line))
            tools_display = "\n".join(lines)
            message = (
                f"Select tools to install from '{group_key}':\n\n"
                f"{tools_display}\n\n"
                "a. Install All\n"
                "0. Cancel\nSelect multiple numbers separated by commas (e.g. 1,3,5) or 'a' for all:"
            )
            from rich.panel import Panel
            self.console.print(Panel(message, title="Tool Selection", border_style="magenta"))
            choice = input("Your choice: ").strip().lower()
            if choice == "0" or choice == "":
                self.console.print("[blue]No tools selected.[/blue]")
                input("Press Enter to continue...")
                return
            if choice == "a":
                if self.system.confirm_prompt("Install ALL tools in this category?"):
                    self.installer.batch_install_and_create_wrappers(tools)
                    self.console.print("[bold green]All tools installed.[/bold green]")
                    input("Press Enter to continue...")
                    return
                else:
                    continue
            parts = choice.split(",")
            selected, valid = [], True
            for part in parts:
                part = part.strip()
                if part.isdigit():
                    idx = int(part)
                    if 1 <= idx <= len(tools):
                        selected.append(tools[idx - 1])
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break
            if not valid or not selected:
                self.console.print("[red]Invalid input. Please enter valid numbers separated by commas or 'a' for all.[/red]")
                input("Press Enter to continue...")
                continue
            self.installer.batch_install_and_create_wrappers(selected)
            self.console.print("[bold green]Installation(s) complete.[/bold green]")
            input("Press Enter to continue...")
            return

    def category_menu(self):
        categories = list(self.data.get_groups().items())
        while True:
            self.system.clear_screen()
            self.system.print_banner()
            self.console.print("[bold magenta]Tool Categories:[/bold magenta]\n")
            for i, (key, desc) in enumerate(categories, 1):
                self.console.print(f"  [green]{i}.[/green] {key} [grey50]- {desc[0]}: {desc[1]}[/grey50]")
            self.console.print("  [green]0.[/green] Back")
            cat_choice = input("\nSelect a category by number: ").strip()
            if cat_choice == "0":
                return
            if not cat_choice.isdigit() or not (1 <= int(cat_choice) <= len(categories)):
                self.console.print("[red]Invalid choice. Try again.[/red]")
                input("Press Enter to continue...")
                continue
            group_key, _ = categories[int(cat_choice)-1]
            tools = self.installer.pacman_group_tools(group_key)
            if not tools:
                self.console.print(f"[yellow]No tools found in {group_key}[/yellow]")
                input("Press Enter to continue...")
                continue
            self.tool_menu(group_key, tools)

    def pentesting_slimiso_menu(self):
        slim_edition = self.data.get_slim_tools()
        while True:
            self.system.clear_screen()
            self.system.print_banner()
            self.console.print("[bold magenta]Pentesting_slim: [/bold magenta]\n")
            for i, tool in enumerate(slim_edition, 1):
                self.console.print(f"  [green]{i}.[/green] {tool}")
            self.console.print("  [green]a.[/green] Install All")
            self.console.print("  [green]0.[/green] Back")
            choice = input("\nSelect tools to install (comma separated, e.g. 1,3,5), 'a' for all, or 0 to go back: ").strip().lower()
            if choice == "0" or choice == "":
                return
            if choice == "a":
                if self.system.confirm_prompt("Install ALL pentesting slim tools?"):
                    self.installer.batch_install_and_create_wrappers(slim_edition)
                    self.console.print("[bold green]All tools installed.[/bold green]")
                    input("Press Enter to continue...")
                    return
                else:
                    continue
            parts = choice.split(",")
            selected, valid = [], True
            for part in parts:
                part = part.strip()
                if part.isdigit():
                    idx = int(part)
                    if 1 <= idx <= len(slim_edition):
                        selected.append(slim_edition[idx - 1])
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break
            if not valid or not selected:
                self.console.print("[red]Invalid input. Please enter valid numbers separated by commas or 'a' for all.[/red]")
                input("Press Enter to continue...")
                continue
            self.installer.batch_install_and_create_wrappers(selected)
            self.console.print("[bold green]Installation(s) complete.[/bold green]")
            input("Press Enter to continue...")
            return

    def main_menu(self):
        self.system.clear_screen()
        self.system.print_banner()
        try:
            self.system.run_command("sudo -v")
        except Exception:
            self.console.print("[red]You need sudo privileges to run this script.[/red]")
            sys.exit(1)

        while True:
            self.system.clear_screen()
            self.system.print_banner()
            self.system.print_main_menu()
            choice = input("Choose an option: ").strip().lower()
            if choice in ("0", "q"):
                self.console.print("[bold red]Exiting.[/bold red]")
                sys.exit(0)
            elif choice == "1":
                self.category_menu()
            elif choice == "2":
                if self.system.confirm_prompt("Update system package database?"):
                    self.installer.update_repo()
                    input("Press Enter to continue...")
            elif choice == "3":
                if self.system.confirm_prompt("Install BlackArch repository?"):
                    self.installer.install_blackarch_repo()
            elif choice == "4":
                self.pentesting_slimiso_menu()
            elif choice == "5":
                self.installer.generate_blackarch_menus(self.data.get_groups())
                input("Press Enter to continue...")
            else:
                self.console.print("[red]Invalid choice. Try again.[/red]")
                input("Press Enter to continue...")
