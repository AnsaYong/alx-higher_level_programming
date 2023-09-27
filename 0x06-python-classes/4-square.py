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

        Instantiation with optional size.

        """
        self.size = size    # does this initialize??

    @property
    def size(self):
        """Property getter.

        Retrieves the value (size) from the private instance
        attribute.

        Returns:
            the private instance attribute size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Property setter.

        Checks if size is a positve integer before
        setting the value of the private instance
        atribute. If size is not a positive integer
        it raises exceptions accordingly.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates a square area.

        A public instance method that calculates a
        square area.

        Returns:
            size * size
        """
        return (self.size * self.size)
