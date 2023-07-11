#!/usr/bin/python3
""" Modules that reads a text file """


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
        filename (str): The name of the file to read (default is empty string).
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')
