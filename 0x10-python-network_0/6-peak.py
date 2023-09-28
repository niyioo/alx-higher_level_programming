#!/usr/bin/python3
"""
This module provides a function to find
a peak in an unsorted list of integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in an unsorted list of
    integers using a binary search algorithm.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int: A peak element from the list.

    Notes:
        A peak element is defined as an element that is
        greater than or equal to its neighbors.

    Complexity:
        The algorithm has a time complexity of O(log(n)).

    Example:
        >>> find_peak([1, 2, 4, 6, 3])
        6
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # The peak must be on the left side
            right = mid
        else:
            # The peak must be on the right side
            # (or current element is part of the peak)
            left = mid + 1

    return list_of_integers[left]
