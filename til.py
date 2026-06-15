# TIL (Today I learned app)

import click
import json
import datetime as dt
import os
from pprint import pprint

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
    # Handle missing or empty file safely
    if os.path.exists("til.json") and os.path.getsize("til.json") > 0:
        with open("til.json", "r") as file:
            file_data = json.load(file)
    else:
        file_data = []

    # handle if tag is left out or not
    actual_tag = tag if tag else "Misc"

    # craete a dict to handle log data 
    new_log = {
        "tag": actual_tag,
        "log": log,
        "datestamp": dt.datetime.now().isoformat()
    }

    file_data.append(new_log)

    with open("til.json", "w") as file:
        json.dump(file_data, file, indent=4)

    click.echo("Notes logged!")

@cli.command()
def list():
    # Handle missing or empty file safely
    if os.path.exists("til.json") and os.path.getsize("til.json") > 0:
        with open("til.json", "r") as file:
            file_data = json.load(file)
    else:
        click.echo("You have no data in your TIL.json, maybe add something you learned today!")
        pass
    
    if file_data:
        pprint(file_data)

if __name__ == "__main__":
    cli()