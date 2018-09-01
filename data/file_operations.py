"""This module contains functions relating to the writing and loading of
files on local storage"""

import json

def write_json(data, path):
    """Export JSON data to UTF-8 encoded .txt file at location 'path'"""
    with open(path, 'w') as file:
        json.dump(data, file, ensure_ascii=False)

def read_json(path):
    """Import JSON response from .txt file located at 'path'"""
    with open(path, 'r') as file:
        data = json.load(file)
    return(data)
