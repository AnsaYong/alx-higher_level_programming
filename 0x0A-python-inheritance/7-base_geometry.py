#!/usr/bin/python3
"""
A module that provides a class
BaseGeometry. It computes calculations
for simple geometries.
"""


class BaseGeometry:
    """
    A class that computes simple
    geometry.
    """
    def area(self):
        """
        A public instance method which raises
        an exception.

        Raises:
            Exception: as long as area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if value is a positive integer. Raises an
        exception.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is a negative integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
