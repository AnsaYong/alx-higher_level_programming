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

    def __str__(self):
        """
        Overrides the __str__ method in the Rectangle
        class. It creates a new string whose format is
        [Square] (<id>) <x>/<y> - <size>.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
