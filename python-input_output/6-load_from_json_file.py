#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an Object from a JSON file.

    Args:
        filename (str): the name of the file to read from.
    """
    with open(filename, mode="r") as f:
        return json.load(f)
