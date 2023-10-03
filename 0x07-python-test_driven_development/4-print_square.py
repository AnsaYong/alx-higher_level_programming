#!/usr/bin/python3
"""
This module provides the print_square function.
It uses ``#`` to print a square whose dimension
is provided by the user.
"""


def print_square(size):
    """Prints a square.

    The dimension of the square is ``size`` and must be
    a number.

    Args:
        size: a number specifiying the size of the square

    Raises:
        TypeError: if size is not an integer, including if
            it is a float and is less than 0
        ValueError: if size is negative

    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):   # rows
        for j in range(size):   # columns
            print("#", end="")
        print()
