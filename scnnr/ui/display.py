from rich.console import Console

console = Console()

def success(msg: str):
  console.print(f"[bold green] {msg}[/bold green]")

def warning(msg: str):
  console.print(f"[bold yellow] {msg}[/bold yellow]")

def error(msg: str):
  console.print(f"[bold red]{msg}[/bold red]")