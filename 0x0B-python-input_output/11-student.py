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

    def to_json(self, attrs=None):
        """ This method etrieves a dictionary representation
            of a Student instance (same as 8-class_to_json.py):
            If attrs is a list of strings,
                  only attribute names contained in this list must be retrieved

            Otherwise, all attributes must be retrieved

        args:
            attrs : attributes
        """
        obj = self.__dict__.copy()

        if type(attrs) is list:

            for attr in attrs:
                if type(attr) is not str:
                    return obj

            my_dict = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        my_dict[satr] = obj[satr]
            return my_dict

        return obj

    def reload_from_json(self, json):
        """ This method replaces all attributes of the Student instance
        args:
            json (dict): json representation of a dict"""
        for attr in json:
            self.__dict__[attr] = json[attr]
