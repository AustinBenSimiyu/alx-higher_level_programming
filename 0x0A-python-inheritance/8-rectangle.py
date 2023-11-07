#!/usr/bin/python3
"""
Class:
    Rectagle: inherits from BaseGeometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class defines BaseGeometry Class to define a rectangle """

    def __init__(self, width, height):
        """ This method initializes an instance of the class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
