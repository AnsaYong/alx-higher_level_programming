#!/usr/bin/python3
"""
This module provides a function that multiplies 2 matrices.
Both matrices must only contain integers or floats.
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices and returns the product.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        matrix

    Raises:
        TypeError: if either m_a or m_b is not a list or list of lists,
            one element of m_a/m_b is not an integer or float, or m_a/m_b
            have rows of different sizes.
        ValueError: one of m_a or m_b is empty or both matrices cannot be
            multiplied
    """
    # check if m_a and m_b are lists
    if not isinstance(m_a, list):   # check entire variable
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # check if each element in m_a and m_b is a list
    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):    # check each row
            raise TypeError("m_a must be a list of lists")
    for j in range(len(m_b)):
        if not isinstance(m_b[j], list):    # check each row
            raise TypeError("m_b must be a list of lists")

    # check if m_a or m_b is empty
    i = 0
    j = 0
    for i in range(len(m_a)):
        if len(m_a[i]) == 0:
            raise ValueError("m_a can't be empty")
    for j in range(len(m_b)):
        if len(m_b[j]) == 0:
            raise ValueError("m_b can't be empty")

    # check if all elements are either integers or floats
    i = 0   # Resetting the value of i to 0
    j = 0   # Resetting the value of j to 0
    for i in range(len(m_a)):   # each row
        for j in range(len(m_a[i])):    # each element in row
            if not isinstance(m_a[i][j], (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for x in range(len(m_b)):
        for y in range(len(m_b[x])):
            if not isinstance(m_b[x][y], (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # check if both matrices have rows of the same size
    i = 0
    j = 0
    for i in range(len(m_a) - 1):
        if len(m_a[i]) - len(m_a[i + 1]) != 0:
            raise TypeError("each row of m_a must be of the same size")
    for j in range(len(m_b) - 1):
        if len(m_b[j]) - len(m_b[j + 1]) != 0:
            raise TypeError("each row of m_b must be of the same size")

    # check if m_a and m_b can be multiplied i.e. columns in m_a = rows in m_b
    if len(m_a[0]) - len(m_b) != 0:
        raise ValueError("m_a and m_b can't be multiplied")

    # if all checks are successful, perform matrix multiplication
    i = 0
    j = 0

    # initialize the result matrix with zeros dynamically
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    # rows of m_a
    for i in range(len(m_a)):
        # columns of m_b
        for j in range(len(m_b)):
            # rows of m_b (or columns of m_a)
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
