#!/usr/bin/python3
""" Module that writes a string """


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to write (default is empty string).
        text (str): The string to write to the file (default is empty string).

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
