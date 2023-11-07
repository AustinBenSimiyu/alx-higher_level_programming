#!/usr/bin/python3
""" This module contains a function that returns
    an object (Python data structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """ This function returns an object represented by a JSON string:

    Args:
        my_str (string): JSON string representation of an object

    Raises:
        Exception: when it fails to decode string
    """
    return (json.loads(my_str))
