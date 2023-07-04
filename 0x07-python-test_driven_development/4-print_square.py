#!/usr/bin/python3
""" Module that print square """


def print_square(size):
    """
    Prints a square with the character '#' of the given size.

    :param size: The size length of the square.
    :raises TypeError: If size is not an integer or a float.
    :raises ValueError: If size is less than 0.
    """

    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        for _ in range(size):
            print("#" * size)
    elif isinstance(size, float):
        raise TypeError("size must be an integer")
    else:
        raise TypeError("size must be an integer")
