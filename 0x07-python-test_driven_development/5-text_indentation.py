#!/usr/bin/python3
"""
This module provides a function that prints
text with 2 new lines after each of the
following characters: ``.``, ``?``, and ``:``
"""


def text_indentation(text):
    """Prints new indented text.

    The function raises an error if text is not
    a string.

    Args:
        text: string to be printed

    Raises:
        TypeError: if text is not a string

    """
    output_string = ""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # first replace all chars of interest
    for char in text:
        if char == '.':
            output_string += '.\n\n'
        elif char == '?':
            output_string += '?\n\n'
        elif char == ':':
            output_string += ':\n\n'
        else:
            output_string += char

    output_lines = output_string.split('\n')    # break up text at newline char

    i = 0
    for line in output_lines:
        i += 1
        stripped_line = line.strip()   # remove trailing whitespace
        print("{}".format(stripped_line),
              end="" if i == len(output_lines) else '\n')
