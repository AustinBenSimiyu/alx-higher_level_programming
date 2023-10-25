#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """Class Square that defines a square
    """

    def __init__(self, size=0):
        """ Method to initialize the square object

        Args:
            size (int): This defines the size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    @property
    def size(self):
        """This method returns the size of a square."""
        return (int(self.size))

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
        return (int(self.__size) ** 2)

    def my_print(self):
        """ Method that prints a # square
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
