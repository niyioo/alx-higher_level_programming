#!/usr/bin/python3
""" Module that returns an object """


import json


def from_json_string(my_str):
    """
    Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        Any: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
