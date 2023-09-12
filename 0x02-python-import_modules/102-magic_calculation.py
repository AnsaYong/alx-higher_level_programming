#!/usr/bin/python3
"""
The given Python bytecode appears to be implementing a function
magic_calculation with two import statements for the add and sub
functions from a module named magic_calculation_102. The function
takes two arguments a and b and performs different operations based
on a comparison between a and b.
"""

from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
