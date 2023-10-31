#!/usr/bin/python3
"""
This is a module that containts a clas that prevents the user
from creating new instance attributes,
except if the attribute is called 'first_name'
"""


class LockedClass:
    """Class LockedClass defines a class that prevents the user
    from creating new instance attributes
    """
    __slots__ = ['first_name']

    def __init__(self):
        """ Method that initilizes an object of the class"""
        pass
