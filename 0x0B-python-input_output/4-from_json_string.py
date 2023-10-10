#!/usr/bin/python3
"""
This module provides a function that returns the
python data structure represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string to its python data
    structure.

    Args:
        my_str: json object to be converted

    Returns:
        python data structure
    """
    return json.loads(my_str)
