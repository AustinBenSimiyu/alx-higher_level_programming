#!/usr/bin/python3
""" This module returns the dictionary description with a simple
    data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ This function retuns the dictionary description of an object """

    dict_desc = {}
    if hasattr(obj, "__dict__"):
        dict_desc = obj.__dict__.copy()
    return (dict_desc)
