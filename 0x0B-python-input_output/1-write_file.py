#!/usr/bin/python3
"""This module has a function that writes a string file"""


def write_file(filename="", text=""):
    """ This function writes text to a file

    Args:
        filename (string): Name of input file
        text (string): Output text

    Raises:
        Exception: When file fails to open
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
