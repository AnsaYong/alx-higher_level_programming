#!/usr/bin/python3
"""

This module provides a function that divides all elements
of a matrix by a given number.

"""


def matrix_divided(matrix, div):
    """Divides elements of matrix by div.

    All elements of matrix must be integers or floats.
    All rows of the matrix must be of the same size.
    div must be an integer or float but cannot be 0.

    Args:
        matrix: a matrix whose elements are to be
            divided
        div: integer by which to divide the elements
            of matrix

    Returns:
        a new matrix of the same dimensions

    Raises:
        TypeError: if any element in matrix is not an
                integer or float, div is not an integer
                or float, or the rows of matrix do not
                have the same length
        ZeroDivisionError: if the parameter div is 0
    """

    # Check if each element in the matrix is integer/float
    for i in range(len(matrix)):    # rows
        for j in range(len(matrix[i])):     # columns
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")

    # Check if all rows in the matrix have the same length
    for row in range(len(matrix) - 1):
        if (len(matrix[row]) - len(matrix[row + 1])) != 0:
            raise TypeError("Each row of the matrix must " +
                            "have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_div = []

    for i in range(len(matrix)):
        row_result = []     # Initialize a list for the current row
        for j in range(len(matrix[i])):
            row_result.append(round(matrix[i][j] / div, 2))     # round to 2 dp
        matrix_div.append(row_result)

    return (matrix_div)
