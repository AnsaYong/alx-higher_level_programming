#!/usr/bin/python3
"""Module to calculate a square.

This module creates a class that defines a square.
The class is empty for now.

"""


class Square:
    """Class Square

    Defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization method.

        Instantiation with optional size and optional
        position.

        """
        self.size = size    # does this initialize??
        self.position = position

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

    @property
    def position(self):
        """Retriever.

        Retrieves the value position from the private
        instance attribute.

        Returns:
            the private instance attribute position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter.

        Checks if value is a 2-positional tuple and then
        sets the position private instance attribute, or
        raises an exception.

        Raises:
            TypeError: if tuple does not have 2 positive integers
        """
        if not isinstance(value, tuple) \
                or len(value) != 2 \
                or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple "
                            "of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates a square area.

        A public instance method that calculates a
        square area.

        Returns:
            size * size
        """
        return (self.size * self.size)

    def my_print(self):
        """Prints a square.

        Prints a square with dimensions size, using
        the '#' characater.
        """
        if self.size == 0:
            print("\n", end="")
        else:
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("{}".format("#"), end="")
                print("\n", end="")
