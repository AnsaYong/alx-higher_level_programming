#!/usr/bin/python3
"""
This module provides a class which will be
the base class.
"""
import json


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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries

        Returns:
            JSON string representation of list_dictionaries
            or []
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries, default=str)
        else:
            return "[]"
