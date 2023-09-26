#!/usr/bin/python3
"""Module docstring.

This module creates a class that defines a square.
The class is empty for now.

"""


class Square:
    """Class Square

    Defines a square.
    """
    def __init__(self, size=0):
        """Initialization method.

        Optionally instantiates a private instance attribute
        with the argument size. If the provided size is
        negative or not an integer, an exception is raised.
        If noo size is given, the private attribute is set
        to 0.

        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is negative

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
