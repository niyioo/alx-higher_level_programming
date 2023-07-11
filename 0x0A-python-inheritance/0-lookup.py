#!/usr/bin/python3
""" module for lookup """


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list of attributes and methods.

    """
    return dir(obj)
