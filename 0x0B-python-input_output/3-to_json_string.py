#!/usr/bin/python3
"""This module has a function that returns
   the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """ This function that returns the JSON representation of an object

    Args:
        my_obj (object): Object to returned in JSON

    Raises:
        Exception: when it fails to encode object
    """
    return (json.dumps(my_obj))
