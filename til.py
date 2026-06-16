# TIL (Today I learned app)

from rich.console import Console
from rich.table import Table
from storage import save_entries, load_entries, make_table
import click
import datetime as dt

# global variables
til_file = "til.json"

@click.group()
def cli():
    pass

@cli.command()
@click.option('--tag', type=click.STRING, help='Creates a tag to allow for searching.')
@click.version_option("1.0", prog_name="til")
@click.argument("log", type=click.STRING)
def add(log, tag):
    """This adds a log to the TIL.json"""
    click.echo("Logging your notes...")

    file_data = load_entries(til_file)


    entries_list = file_data["entries"]

    # If the file has data, extract the largest ID. Otherwise, start at 0.
    if entries_list:
        largest_id = max(item.get("id", 0) for item in entries_list)
    else:
        largest_id = 0

    next_id = largest_id + 1
    # handle if tag is left out or not
    actual_tag = tag if tag else "Misc"
    
    # craete a dict to handle log data 
    new_log = {
        "id" : next_id,
        "tag": actual_tag,
        "log": log,
        "datestamp": dt.datetime.now().strftime("%Y-%m-%d")
    }

    entries_list.append(new_log)

    save_entries(til_file, file_data)

    click.echo("Notes logged!")

@cli.command()
def list():
    """Lists all entries in json file"""

    # load data
    file_data = load_entries(til_file)
    entries = file_data.get("entries", [])
    
    make_table(entries)

@cli.command()
@click.argument("query", type=click.STRING)
def search(query):
    """This allows to query the logs, the query will be log text only, / 
    it should also have options, so you can filter on tag, date, and id"""
    file_data = load_entries("til.json")

    entries = file_data.get("entries", [])

    matching_logs = [
        item for item in entries 
        if query.lower() in item.get("log", "").lower()
        ]
    
    make_table(matching_logs)

@cli.command()
def stats():
    """This shows the number of entries, count of entries per tag, and /
    A simple streak: how many consecutive days you've logged something"""

if __name__ == "__main__":
    cli()