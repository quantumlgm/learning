import argparse
import json
import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

console = Console()
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "greetings.json")

DEFAULT_GREETINGS = [
    "Hello world!",
    "Hello USA",
    "Hello Novorossiysk",
    "Catch me up man!"
]

def load_greetings():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_GREETINGS.copy()

def save_greetings(greetings):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(greetings, f, ensure_ascii=False, indent=4)

def show_greeting(greetings):
    if not greetings:
        console.print("[red]No greetings available![/red]")
        return
    greeting = random.choice(greetings)
    text = Text(greeting, style="bold magenta", justify="center")
    panel = Panel(text, title="Random Greeting", expand=False, border_style="cyan")
    console.print(panel)

def list_greetings(greetings):
    table = Table(title="Available Greetings")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Greeting", style="magenta")

    for i, greeting in enumerate(greetings):
        table.add_row(str(i), greeting)

    console.print(table)

def add_greeting(greetings, new_greeting):
    greetings.append(new_greeting)
    save_greetings(greetings)
    console.print(f"[green]Added:[/green] {new_greeting}")

def edit_greeting(greetings, idx, new_greeting):
    if 0 <= idx < len(greetings):
        old = greetings[idx]
        greetings[idx] = new_greeting
        save_greetings(greetings)
        console.print(f"[green]Edited:[/green] {old} -> {new_greeting}")
    else:
        console.print(f"[red]Invalid index: {idx}[/red]")

def delete_greeting(greetings, idx):
    if 0 <= idx < len(greetings):
        removed = greetings.pop(idx)
        save_greetings(greetings)
        console.print(f"[green]Deleted:[/green] {removed}")
    else:
        console.print(f"[red]Invalid index: {idx}[/red]")

def main():
    parser = argparse.ArgumentParser(description="CLI utility for displaying greetings with Rich")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: show (default)
    subparsers.add_parser("show", help="Show a random greeting")

    # Command: list
    subparsers.add_parser("list", help="List all greetings")

    # Command: add
    add_parser = subparsers.add_parser("add", help="Add a new greeting")
    add_parser.add_argument("text", type=str, help="The greeting text to add")

    # Command: edit
    edit_parser = subparsers.add_parser("edit", help="Edit an existing greeting")
    edit_parser.add_argument("index", type=int, help="Index of the greeting to edit")
    edit_parser.add_argument("text", type=str, help="The new greeting text")

    # Command: delete
    delete_parser = subparsers.add_parser("delete", help="Delete a greeting")
    delete_parser.add_argument("index", type=int, help="Index of the greeting to delete")

    args = parser.parse_args()
    greetings = load_greetings()

    if args.command == "list":
        list_greetings(greetings)
    elif args.command == "add":
        add_greeting(greetings, args.text)
    elif args.command == "edit":
        edit_greeting(greetings, args.index, args.text)
    elif args.command == "delete":
        delete_greeting(greetings, args.index)
    else:
        show_greeting(greetings)

if __name__ == "__main__":
    main()
