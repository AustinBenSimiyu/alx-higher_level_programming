#!/usr/bin/python3
""" This module contains a function that writes an Object to a text file,
    using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """ This function that writes an Object to a text file,
        using a JSON representation:

    Args:
        my_obj (object): python object data structure
        filename (string): name of file

    Raises:
        Exception: when it fails to decode object
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
