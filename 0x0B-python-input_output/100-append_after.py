#!/usr/bin/python3
""" Module that inserts a line of text """


def append_after(filename, search_string, new_string):
    """
    Inserts a line of text after each line
    containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matched line.

    Returns:
        None
    """
    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
