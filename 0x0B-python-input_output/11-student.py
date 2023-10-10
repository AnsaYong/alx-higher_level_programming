#!/usr/bin/python3
"""
This module provides a class that defines a student
by first_name, last_name and age
"""


class Student:
    """Class Student
    Defines a student by first_name, last_name and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates the student with their first_name,
        last_name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A public method that retrieves a dictionary
        representation of a student instance

        Args:
            attrs: optional - list of attribute names to be retrieved
        """
        def serialize(obj, selected_attrs):
            """
            Serializes an object.
            """
            if isinstance(obj, dict):
                # If the object is already a dictionary, return it as is
                return obj
            elif isinstance(obj, list):
                # If the object is a list, serialize its elements recursively
                return [serialize(item, selected_attrs) for item in obj]
            elif isinstance(obj, (str, int, bool)):
                # If the object is a string, integer, or boolean, return as is
                return obj
            elif hasattr(obj, '__dict__'):
                # If the object is an instance of a class with attributes,
                # serialize its attributes
                if selected_attrs is None:
                    selected_attrs = obj.__dict__.keys()
                serialized = {}
                for key, value in obj.__dict__.items():
                    if key in selected_attrs:
                        serialized[key] = serialize(value, selected_attrs)
                return serialized
            else:
                # If the object doesn't fit any known type, return None
                return None

        return serialize(self.__dict__, attrs)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance.

        Args:
            json: a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
