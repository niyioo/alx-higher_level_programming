#!/usr/bin/python3
""" module for text indentation """


def text_indentation(text):
    """
    Prints the given text with 2 new lines after each occurrence of '.', '?', and ':'.

    :param text: The text as a string.
    :raises TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    result = ''
    for char in text:
        result += char
        if char in punctuation_marks:
            result += '\n\n'

    print(result.strip())
