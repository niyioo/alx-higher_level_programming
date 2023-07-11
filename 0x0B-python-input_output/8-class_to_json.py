#!/usr/bin/python3
""" Module that returns dictionary desc """


def class_to_json(obj):
    """
    Return the dictionary description of an object with a simple data structure suitable for JSON serialization.

    Args:
        obj (object): The object to convert to a dictionary.

    Returns:
        dict: The dictionary description of the object.
    """
    obj_dict = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attr] = value
    return obj_dict
