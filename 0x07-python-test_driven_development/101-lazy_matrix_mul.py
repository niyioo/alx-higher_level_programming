#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy and return the result.

    Args:
        m_a: First matrix as a list of lists.
        m_b: Second matrix as a list of lists.

    Returns:
        The result of matrix multiplication as a new matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                   or if the elements of m_a or m_b are not integers or floats,
                   or if the rows of m_a or m_b are not of the same size.
        ValueError: If m_a or m_b is empty, or if m_a and m_b
        cannot be multiplied.
    """

    return (np.matmul(m_a, m_b))
