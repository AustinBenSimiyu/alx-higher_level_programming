#!/usr/bin/python3
"""
Class:
    Rectagle: inherits from BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class inherits from BaseGeometry Class to define a rectangle"""

    def __init__(self, width, height):
        """ This method initializes an instance of the class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ This method returns the area of the object"""
        return (self.__width * self.__height)

    def __str__(self):
        """ This method returns a printable string """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
