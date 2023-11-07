#!/usr/bin/python3
"""
Function:
    lookup: returns list of available attributes.
"""


def lookup(obj):
    """ This Function returns the list of available attributes
        and methods of an object
    Args:
        obj: instance of the class
    Returns:
        List of attributes
    """

    return dir(obj)
