#!/usr/bin/python3
"""
This module provides the ``say_my_name`` function. The
function prints the first and last names provided by
the user.
"""


def say_my_name(first_name, last_name=""):
    """Prints the user's first and last name.

    Names must be strings.

    Args:
        first_name: user's first name
        last_name: user's last name

    Returns:
        Nothing - Prints a sentence to stdout

    Raises:
        TypeError: if either first or last name is
            not a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
