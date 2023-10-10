#!/usr/bin/python3
"""
This module provides a function that returns the
JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Converts an object to its json representation

    Args:
        my_obj: object to be converted

    Returns:
        json representation of my_obj
    """
    return json.dumps(my_obj)
