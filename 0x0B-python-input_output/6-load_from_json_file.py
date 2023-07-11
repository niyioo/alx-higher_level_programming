#!/usr/bin/python3
""" Module that creates an Object """


import json

def load_from_json_file(filename):
    """
    Load a Python object (data structure) from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        Any: The Python object (data structure) loaded from the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
