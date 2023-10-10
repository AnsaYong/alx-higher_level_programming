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

    def to_json(self):
        """
        A public method that retrieves a dictionary
        representation of a student instance
        """
        def serialize(obj):
            """
            Serializes an object.
            """
            if isinstance(obj, dict):
                # If the object is already a dictionary, return it as is
                return obj
            elif isinstance(obj, list):
                # If the object is a list, serialize its elements recursively
                return [serialize(item) for item in obj]
            elif isinstance(obj, (str, int, bool)):
                # If the object is a string, integer, or boolean, return as is
                return obj
            elif hasattr(obj, '__dict__'):
                # If the object is an instance of a class with attributes,
                # serialize its attributes
                serialized = {}
                for key, value in obj.__dict__.items():
                    serialized[key] = serialize(value)
                return serialized
            else:
                # If the object doesn't fit any known type, return None
                return None

        return serialize(self.__dict__)
