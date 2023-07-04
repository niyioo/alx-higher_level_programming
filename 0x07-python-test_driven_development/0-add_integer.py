#!/usr/bin/python3
""" integer addition function module """


def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: An integer or float.
    :param b: An integer or float (default: 98).
    :return: The addition of a and b as an integer.
    :raises TypeError: If a or b is not an integer or float.

    Examples:
    >>> add_integer(5, 10)
    15
    >>> add_integer(2.5, 3.7)
    6
    >>> add_integer(3, 4.5)
    7
    >>> add_integer(2, '3')
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or b must be an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
