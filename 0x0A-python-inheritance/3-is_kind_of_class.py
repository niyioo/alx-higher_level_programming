#!/usr/bin/python3
""" Module for same class or inherit from  """


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, the specified class.

    Args:
        obj: An object.
        a_class: A class to compare against.

    Returns:
        True if the object is an instance of, or inherited from, the specified class,
        False otherwise.

    """
    return isinstance(obj, a_class)
