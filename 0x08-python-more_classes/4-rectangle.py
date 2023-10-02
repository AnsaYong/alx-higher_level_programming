#!/usr/bin/python3
"""This module provides an empty class
The class is called Rectangle.
"""


class Rectangle:
    """Class Rectangle
    Defines a Rectangle and performs operations.
    """
    def __init__(self, width=0, height=0):
        """Initialization method

        Initiates private instance attributes
        (field in this case), width and height.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
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

    def area(self):
        """Calculates the area of a rectangle.

        Returns:
            the area
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a rectangle.

        Returns:
            the perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """string representation method
        Returns a strng representation of the Rectangle object
        using '#' to show the shape.
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.height):    # _ represents unused. set height
            rectangle_str += "#" * self.width + "\n"

        return rectangle_str.rstrip("\n")   # remove trailing newline

    def __repr__(self):
        """Representation method
        Returns a string representation of the Rectangle object
        that can be used with eval() to recreate the object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)
