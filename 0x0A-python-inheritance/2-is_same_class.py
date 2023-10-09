#!/usr/bin/python3
"""
This module provides a method that checks if
a given object is excatly an instance of
a given class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance
    of a class or not.

    Args:
        obj: the object
        a_class: the class
    Returns:
        True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
