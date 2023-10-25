#!/usr/bin/python3
""" Class Square definesa square object"""


class Square:
    """Class Square that defines a square object

    This class has no public attributes
    """
    def __init__(self, size):
        """Initialize method that stores the size of the square

        Args:
             size (int): Defines size of square
        """
        self.__size = size
