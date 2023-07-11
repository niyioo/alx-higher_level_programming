#!/usr/bin/python3
""" Module that writes an Object """


import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj (Any): The object to write to the file.
        filename (str): The name of the file to write.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
