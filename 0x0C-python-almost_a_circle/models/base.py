#!/usr/bin/python3
"""
This module provides a class which will be
the base class.
"""


class Base:
    """
    The Base class has a private attribute
    which will be used to set ``id`` when
    it is not given.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class based on
        the value of the ``id`` argument.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
