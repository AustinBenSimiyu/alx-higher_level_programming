#!/usr/bin/python3
"""
Class:
    Square: inherits from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class inherits rectangle class to define a square """

    def __init__(self, size):
        """ This method initializes a square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ This method that returns the area """
        return (super().area())
