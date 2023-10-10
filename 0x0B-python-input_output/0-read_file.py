#!/usr/bin/python3
"""
This module provides a function that reads a text
file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a utf-8 text file and prints the
    contents to stdout.

    Args:
        filename: text file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print("{}".format(f.read()), end="")
