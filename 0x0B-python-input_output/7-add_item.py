#!/usr/bin/python3
""" Module that adds all arguments to list """


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    """Load existing data from the file, if it exists"""
    data = load_from_json_file(filename)
except FileNotFoundError:
    """If the file doesn't exist, initialize an empty list"""
    data = []

"""Add command-line arguments to the list"""
data.extend(sys.argv[1:])

"""Save the updated list as a JSON representation in the file"""
save_to_json_file(data, filename)
