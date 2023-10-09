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
        if type(value) is not int or value is None:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class Rectangle.
    Inherits __from class BaseGeometry
    and defines a square.
    """
    def __init__(self, width, height):
        """Initialization method

        Instantiates with width and height as
        private instances.
        """
        super().__init__()  # Create an instance of BaseGeometry
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle

        Returns:
            the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the
        rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
