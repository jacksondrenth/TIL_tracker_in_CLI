# Storage.py

import json
import os

def load_entries(file_path):
    """Loads content of a json file"""
    if os.path.exists(file_path) and os.path.getsize("til.json") > 0:
        with open(file_path, "r") as file:
                file_data = json.load(file)
    else:
        file_data = {"entries": []}
    return file_data


def save_entries(file_path, contents):
    """Saves contents to a json file"""
    with open(file_path, "w") as file:
        json.dump(contents, file, indent=4)