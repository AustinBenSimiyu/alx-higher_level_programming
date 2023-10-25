#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """Class Square that defines a square

    This class has no public attributes

    """

    def __init__(self, size=0):
        """ Method to initialize the square object

        Args:
             size (int): This defines size of square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
