#!/usr/bin/python3
"""
This module provides a function that returns the
dictionary description with simple data structure
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data
    structure for JSON serialization.

    Args:
        obj: an instance of a Class
    """
    if isinstance(obj, dict):
        # If the object is already a dictionary, return it as is
        return obj
    elif isinstance(obj, list):
        # If the object is a list, serialize its elements recursively
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, (str, int, bool)):
        # If the object is a string, integer, or boolean, return it as is
        return obj
    elif hasattr(obj, '__dict__'):
        # If the object is an instance of a class with attributes,
        # serialize its attributes
        serialized = {}
        for key, value in obj.__dict__.items():
            serialized[key] = class_to_json(value)
        return serialized
    else:
        # If the object doesn't fit any known type, return None
        return None
