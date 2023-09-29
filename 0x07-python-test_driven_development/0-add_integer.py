#!/usr/bin/python3
"""

This module provides a function, add_integers. The
function adds two integers or floats and returns
the integer sum.

"""


def add_integer(a, b=98):
    """Adds two numbers.

    Args:
        a (int): The first parameter
        b (int): The second parameter

    Returns:
        an integer: the sum of `a` and `b`

    Raises:
        TypeError: if either `a` or `b` is not an integer or float

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
