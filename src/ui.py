from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()


def clear_screen() -> None:
    console.clear()


def load_skull() -> str:
    skull_path = Path("assets") / "skull.txt"
    if skull_path.exists():
        return skull_path.read_text(encoding="utf-8")
    return "PIRATE ESSENTIALS"


def show_intro(items: list[str]) -> None:
    clear_screen()
    console.print(load_skull(), style="bold white")
    console.print("[bold red]Pirate Essentials[/bold red]")
    console.print("Utility for installing an essential programming environment.\n")

    console.print("[bold yellow]Warning:[/bold yellow]")
    console.print("- Administrator privileges may be required.")
    console.print("- Internet connection is required.")
    console.print("- Some packages may take several minutes to install.")
    console.print("- The tool installs Git and Python libraries for development in a local .venv.\n")

    console.print("[bold]The following components will be installed:[/bold]")
    for item in items:
        console.print(f" - {item}")


def ask_confirmation() -> bool:
    while True:
        answer = input("\nStart installation? (Y/N): ").strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        console.print("Please enter Y or N.", style="bold red")


def show_install_header(total_steps: int) -> None:
    clear_screen()
    console.print("[bold red]Pirate Essentials[/bold red]")
    console.print(f"Installing components... Total steps: {total_steps}\n")


def show_results(successful: list[str], failed: list[str]) -> None:
    clear_screen()
    console.print("[bold red]Pirate Essentials[/bold red]")
    console.print("[bold]Installation completed.[/bold]\n")

    table = Table(show_header=True, header_style="bold")
    table.add_column("Component", width=40)
    table.add_column("Status", width=10)

    for item in successful:
        table.add_row(item, "[green]Y[/green]")

    for item in failed:
        table.add_row(item, "[red]N[/red]")

    console.print(table)
    console.print()
    console.print("Questions or problems:")
    console.print("https://github.com/ALEXPAN-DEV")
    input("\nPlease press Enter to exit...")