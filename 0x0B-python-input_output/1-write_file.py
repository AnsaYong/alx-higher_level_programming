#!/usr/bin/python3
"""
This module provides a function that writes a string
to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number
    of characters written.

    Args:
        filename: the file to be read
        text: string to write to text

    Returns:
        number of characters read
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
