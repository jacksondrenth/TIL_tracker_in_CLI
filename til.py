# TIL (Today I learned app)

import click
import json
import datetime as dt
import os

@click.group()
def cli():
    pass

@click.command()
@click.option('--tag', type=click.STRING, help='Creates a tag to allow for searching.')
@click.version_option("1.0", prog_name="til")
@click.argument("log")
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

if __name__ == "__main__":
    cli()