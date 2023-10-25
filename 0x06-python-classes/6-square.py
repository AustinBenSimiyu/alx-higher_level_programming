#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """Class Square that defines a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object

        Args:
            size (int): This defines the size of the square.

            position (tuple): This defines the position of the square.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object

        Args:
            value (tuple): this tuple defines the position of the square.

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
