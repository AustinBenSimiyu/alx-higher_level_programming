#!/usr/bin/python3
""" This module defines a Student class
"""


class Student:
    """ Class student defines student instances """

    def __init__(self, first_name, last_name, age):
        """ This method initializes a student instance

        Args:
             first_name (string): student first name
             last_name (string): student last name
             age (int): student age

        Raises:
             None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This method that returns a dictionary description """
        return (self.__dict__.copy())
