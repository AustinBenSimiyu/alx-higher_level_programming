#!/usr/bin/python3
"""
Class:
    BaseGeometry: defines the geometry of a shape
"""


class BaseGeometry:
    """ This class defines the area of a shape"""
    def area(self):
        """ This method defines the area of a shape """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This method raises an exception if the property is not validated
        Args:
            name: name of property
            value: value of the property
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
