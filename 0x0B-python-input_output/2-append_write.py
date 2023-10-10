#!/usr/bin/python3
"""
This module provides a function that appends a string
at the end of a text file and returns the number of
characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of as file and
    returns the number of characters added.

    Args:
        filename: file to be appended to
        text: string to append

    Returns:
        number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_text = f.write(text)

    return append_text
