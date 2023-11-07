#!/usr/bin/python3
""" This module contains a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ This function that creates an Object from a “JSON file”:

    Args:
        filename (string): name of file

    Raises:
        Exception: when it fails to encode object
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
