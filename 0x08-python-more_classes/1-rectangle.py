#!/usr/bin/python3
"""This module provides an empty class
The class is called Rectangle.
"""


class Rectangle:
    """Class Rectangle
    Defines a Rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initialization method

        Initiates private instance attributes
        (field in this case), width and height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property getter
        Retrieves width from the private instance
        attribute.

        Returns:
            the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter.
        Sets the private instance attribute width.
        width must be a positive integer

        Args:
            value: width of rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property getter - height
        Retrieves the private instance attribute height.

        Returns:
            the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        If height is not a positive integer,
        it raises an exception.

        Args:
            value: represents the height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
