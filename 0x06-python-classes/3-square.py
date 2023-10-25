#!/usr/bin/python3
""" Class square defines a square"""


class Square:
    """Class Square that defines a square
    """

    def __init__(self, size=0):
        """This method initiates a square.

        Args:
            size (int): This defines the size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """ Method that returns the area of a square
        """
        return (int(self.__size) ** 2)
