#!/usr/bin/python3
""" Module that appends a string """


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and
    return the number of characters added.

    Args:
        filename (str): The name of the file to append
        (default is empty string).
        text (str): The string to append to the file (default is empty string).

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
