#!/usr/bin/python3

"""
Module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    :param matrix: A list of lists containing integers or floats.
    :param div: A number (integer or float) to divide the matrix elements by.
    :return: A new matrix with elements divided by div,
    rounded to 2 decimal places.
    :raises TypeError: If matrix is not a matrix (list of lists)
    of integers or floats,
                       or if each row of the matrix doesn't have the same size,
                       or if div is not a number.
    :raises ZeroDivisionError: If div is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
