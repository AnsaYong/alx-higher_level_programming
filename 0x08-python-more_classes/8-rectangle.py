#!/usr/bin/python3
"""This module provides an empty class
The class is called Rectangle.
"""


class Rectangle:
    """Class Rectangle
    Defines a Rectangle and performs operations.
    """
    # public class attribute
    number_of_instances = 0
    print_symbol = "#"

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

        # Increment the instance count when new object is created
        Rectangle.number_of_instances += 1

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
            if isinstance(self.print_symbol, list):
                # first convert list to a string
                list_to_string = "[{}]".format(", ".join(self.print_symbol))
                rectangle_str += list_to_string * self.width + "\n"
            else:
                rectangle_str += self.print_symbol * self.width + "\n"

        return rectangle_str.rstrip("\n")   # remove trailing newline

    def __repr__(self):
        """Representation method
        Returns a string representation of the Rectangle object
        that can be used with eval() to recreate the object.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor method
        Called when an instance of Rectangle is about to be deleted.
        """
        # decrement the instance count whenever an instance is deleted
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to return the bigger or equal rectangle
        based on area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2
