#!/usr/bin/python3
"""
Function:
    add_attributes: adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """ This function adds a new attribute to object

    Args:
        obj: object
        name (string): attribute name
        value (int): attribute value

    Raises:
        TypeError: when the attribute can't be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
