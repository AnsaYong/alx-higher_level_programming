#!/usr/bin/python3
"""
This module provides a method that checks if
a given object is an instance of a given class
or of another class inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance
    of a class or of one inherited from
    it.

    Args:
        obj: the object
        a_class: the class
    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
