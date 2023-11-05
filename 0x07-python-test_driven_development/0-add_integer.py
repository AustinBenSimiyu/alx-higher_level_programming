#!/usr/bin/python3
"""
This module is composed has a function that adds two numbers
"""


def add_integer(a, b=98):
    """ This function adds two integer and/or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The sum of the two arguments
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be a integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
