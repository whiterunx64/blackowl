import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from pyfiglet import Figlet

class System:
    def __init__(self):
        self.console = Console()

    # === UTILITY FUNCTIONS ===
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def run_command(self, cmd, check=True):
        return subprocess.run(cmd, shell=True, check=check)

    def print_banner(self):
        fig = Figlet(font='slant')
        banner = fig.renderText('Black-owl')
        width = getattr(self.console, "width", 80)
        for line in banner.splitlines():
            self.console.print(f"[bold cyan]{line.center(width)}[/bold cyan]")
        name_line = "[bold magenta]Created by[/bold magenta] [bold cyan]whiterunx64[/bold cyan]"
        self.console.print(f"{name_line}")

    def print_main_menu(self):
        menu = """
[bold cyan]Main Menu:[/bold cyan]

[green]1.[/green] BlackArch Tool Categories
[green]2.[/green] Update Database
[green]3.[/green] Install BlackArch Repository
[green]4.[/green] Pentester-slim Toolset
[green]5.[/green] Generate BlackArch Menus
[green]0.[/green] Exit
"""
        self.console.print(Panel(menu.strip(), title="[bold blue]Select an Option[/bold blue]", border_style="cyan"))

    def confirm_prompt(self, prompt: str) -> bool:
        self.console.print(f"[yellow]{prompt} (y/n)[/yellow]")
        while True:
            c = input().strip().lower()
            if c in ("y", "yes"):
                return True
            if c in ("n", "no"):
                return False
