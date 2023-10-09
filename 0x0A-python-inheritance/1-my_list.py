#!/usr/bin/python3
"""
This module provides a class called ``MyList`` and a public
instance method called ``print_sorted``.
"""


class MyList(list):
    """
    A class that inherits from list.
    The class has an additional method
    called print_sorted.
    """
    def print_sorted(self):
        """
        Sorts the list before printing
        it. The original list is not
        changed.
        """
        sorted_list = sorted(self)
        print(sorted_list)
