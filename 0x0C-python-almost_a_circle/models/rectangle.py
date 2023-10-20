#!/usr/bin/python3
"""
This module provides the Rectangle class which
inherits the Base class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Inherits frm the ``Base`` class and then
    initializes width, height, x, and y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes width, height, x, y, of the rectangle
        and then calls on the super class to initialize the
        rectangle id.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = y

        super().__init__(id)  # call the superclass, Base, to set id

    @property
    def width(self):
        """Property getter

        Retrieves the ``width`` attribute

        Returns:
            the private instance attribute width
        """

        return (self.__width)

    @width.setter
    def width(self, width):
        """Property setter

        Sets the private instance ``width``.

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than or equal to 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        Retrieves the height.
        """

        return (self.__height)

    @height.setter
    def height(self, height):
        """
        Sets the height.

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is < or = 0
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        Retrieves the value of x.
        """

        return (self.__x)

    @x.setter
    def x(self, x):
        """
        Sets the value of x.

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is less than 0
        """

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        Retrieves the value of y.
        """

        return (self.__y)

    @y.setter
    def y(self, y):
        """
        Sets the value of y.

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is less than 0
        """

        if not isinstance(y, int):
            raise TypeError("y must be an intger")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        Calculates the area of a rectangle

        Returns:
            width * height
        """

        return (self.__width * self.__height)

    def display(self):
        """
        Prints the rectangle instance using ``#``
        """

        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("{}".format("#"), end="")
            print()

    # Override any previous __str__ method (potentially inherited)
    def __str__(self):
        """
        Setting the __str__ method to return a string
        of type [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """
        A public method that assigns an argument to
        each attribute.

        Args:
            args: "no-keyword argument" - arg order is very important
            kwargs: "key-worded argument" - arg order is not important
        """
        # Order the attributes the way we want them
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            # Since the numb of attributes is set above, this ensures we
            # never try to update more attributes than are present
            no_attr = min(len(args), len(attributes))    # use the smallest
            for i in range(no_attr):
                setattr(self, attributes[i], args[i])   # update in order
        else:
            for attr_name in kwargs:
                if attr_name in attributes:
                    setattr(self, attr_name, kwargs[attr_name])

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle.

        Returns:
            a dictionary containing the attributes of the Rectangle.
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
