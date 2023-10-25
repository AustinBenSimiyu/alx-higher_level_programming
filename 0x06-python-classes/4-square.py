#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """ Class Square that defines a square
    """

    def __init__(self, size=0):
        """This method initiates a square.

        Args:
            size (int): This defines the size of the square.

        """
        self.size = size

    @property
    def size(self):
        """This method returns the size of a square."""
        return (int(self.__size))

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object

        Args:
            size (int): This defines the size of the square.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Method that returns the area of a square
        """
        return (int(self.__size ** 2))
