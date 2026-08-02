from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

text = Text("Hello World!", style="bold magenta", justify="center")
panel = Panel(text, title="Greeting", expand=False, border_style="cyan")

console.print(panel)
