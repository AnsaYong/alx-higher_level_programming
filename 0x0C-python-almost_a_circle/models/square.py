#!/usr/bin/python3

"""
This module provides a Square class which inherits
the Rectangle class, which itself inherited the
Base class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square inherits the Rectangle class. It uses the
    Rectangle methods to initialize its values, including
    validation.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square class by calling
        the superclass.

        Args:
            size: size of the square
            x: x position
            y: y position
            id: square instance/id
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter for the size attribute.
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """
        Overrides the __str__ method in the Rectangle
        class. It creates a new string whose format is
        [Square] (<id>) <x>/<y> - <size>.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """
        A public method that updates the existing
        attributes by assigning new arguments.

        Args:
            args: "no-keyword argument" - arg order is very important
            kwargs: "key-worded argument" - arg order is not important
        """
        attributes = ["id", "size", "x", "y"]

        if args:
            no_attr = min(len(args), len(attributes))
            for i in range(no_attr):
                setattr(self, attributes[i], args[i])
        else:
            for name in kwargs:
                if name in attributes:
                    setattr(self, name, kwargs[name])

    def to_dictionary(self):
        """
        Returns the dictionary representation of a square.

        Returns:
            dictionary of all square attributes.
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
