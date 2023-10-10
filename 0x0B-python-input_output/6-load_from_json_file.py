#!/usr/bin/python3
"""
This module provides a function that creates an object
from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """
    Creates a python data structure from a JSON
    file

    Args:
        filename: the file name of a json file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
