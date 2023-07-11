#!/usr/bin/python3
""" Module for same class or inherit from  """


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class
    that inherited (directly or indirectly) from
    the specified class.

    Args:
        obj: An object.
        a_class: A class to compare against.

    Returns:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from
        the specified class; False otherwise.

    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
