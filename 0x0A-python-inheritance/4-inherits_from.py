#!/usr/bin/python3
"""
This module provides a method that checks if
a given object is an instance of a class
inherited from the given class.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance
    of a class inherited from the given
    class.

    Args:
        obj: the object
        a_class: the class
    Returns:
        True or False
    """
    return isinstance(obj, a_class) and obj.__class__ is not a_class
