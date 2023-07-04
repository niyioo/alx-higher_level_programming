#!/usr/bin/python3
""" module to copy a list object """


def copy_list(l):
    """
    Create a shallow copy of a list.

    Args:
        l (list): The input list.

    Returns:
        list: A shallow copy of the input list.

    Examples:
        >>> my_list = [1, 2, 3]
        >>> new_list = copy_list(my_list)
        >>> print(new_list)
        [1, 2, 3]
        >>> print(new_list == my_list)
        True
        >>> print(new_list is my_list)
        False
    """
    return l[:]
