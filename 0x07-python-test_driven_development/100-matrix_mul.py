#!/usr/bin/python3
"""Module for matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the result.

    Args:
        m_a: First matrix as a list of lists.
        m_b: Second matrix as a list of lists.

    Returns:
        The result of matrix multiplication as a new matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                   or if the elements of m_a or m_b are not integers or floats,
                   or if the rows of m_a or m_b are not of the same size.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or \
       not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or "
                        "m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or \
       not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or "
                        "each row of m_b must be of the same size")

    cols_a = len(m_a[0])
    rows_b = len(m_b)

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(cols_a))
            row.append(element)
        result.append(row)

    return result
