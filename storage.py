# Storage.py

from rich.console import Console
from rich.table import Table
import json
import os
import click

def load_entries(file_path):
    """Loads content of a json file"""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as file:
                file_data = json.load(file)
    else:
        file_data = {"entries": []}
    return file_data


def save_entries(file_path, contents):
    """Saves contents to a json file"""
    with open(file_path, "w") as file:
        json.dump(contents, file, indent=4)

def make_table(entries_list):
    """Function to make tables on given list"""

    if not entries_list:
        click.echo("No entries yet, add something you've learned today!")
        return
    

     # create table
    table = Table(title="TIL Entries")
    # create table columns
    table.add_column("ID", justify="center", style="yellow")
    table.add_column("Datestamp", justify="center", style="cyan", no_wrap=True)
    table.add_column("Log", justify="center", style="magenta")
    table.add_column("Tag", justify="center", style="green")
    
    # create rows
    for entry in entries_list:

        entry_id = str(entry.get("id", ""))
        entry_tag = entry.get("tag", "Misc")
        entry_log = entry.get("log", "")
        entry_date = entry.get("datestamp", "")

        table.add_row(entry_id, entry_date, entry_log, entry_tag)

    console = Console()
    console.print(table)