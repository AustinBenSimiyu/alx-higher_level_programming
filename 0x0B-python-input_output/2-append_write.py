#!/usr/bin/python3
"""This module has a function that writes a string to text file"""


def append_write(filename="", text=""):
    """ This function appends a string to the end of a file

    Args:
        filename (string): Name of input file
        text (string): Output text

    Raises:
        Exception: When file fails to open
    """

    with open(filname, 'a', encoding='utf-8') as f:
        return (f.write(text))
