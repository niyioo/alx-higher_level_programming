#!/usr/bin/python3
""" Module of a function that prints a message """


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    :param first_name: The first name as a string.
    :param last_name: The last name as a string. Default is an empty string.
    :raises TypeError: If first_name or last_name is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name
    if last_name:
        full_name += " " + last_name

    print("My name is", full_name)
