#!/usr/bin/python3

"""
Provides a function that retrieves
the attributes and methods of an
object.
"""

def lookup(obj):
    """
    Retrieves the list of available attributes
    and methods of an object.

    Args:
        obj: object whose attributes and methods
            are required

    Returns:
        list of attributes and methods
    """
    return dir(obj)
