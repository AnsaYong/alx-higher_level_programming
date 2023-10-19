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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A class method that writes the JSON string
        representation of list_objs to a file.

        Args:
            cls: the class
            list_objs: list of instances that inherit
            from Base
        Returns:
            .json file
        """
        if list_objs is None:
            list_objs = []

        # convert each instance in list_objs to a JSON string
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # construct the required filename
        filename = cls.__name__ + ".json"

        # Write the JSON data to file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(list_dicts))
