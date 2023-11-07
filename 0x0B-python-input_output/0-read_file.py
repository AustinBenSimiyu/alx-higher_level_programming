#!/usr/bin/python3
""" Module that reads a file and prints its contents"""


def read_file(filename=""):
    """ This function reads the contents of a file

    Args:
         filename (string): name of the file

    Raises:
         Exception: when it fails to open a file

    """
    with open(filename, 'r', encoding="utf-8") as f:
        file_content = f.read()
        print(file_content, end='')
