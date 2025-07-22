from rich.console import Console
from rich.text import Text

console = Console()

def success(message: str):
    console.print(Text(f"{message}", style="bold green"))

def warning(message: str):
    console.print(Text(f"{message}", style="bold yellow"))

def error(message: str):
    console.print(Text(f"{message}", style="bold red"))

def info(message: str):
    console.print(Text(f"{message}", style="bold blue"))
