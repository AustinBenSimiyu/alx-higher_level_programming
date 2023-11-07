#!/usr/bin/python3
"""
Class:
    MyList: inherits from class list.
"""


class MyList(list):
    """ This class inherits the attributes references of class list
    Args:
        list: class list
    """
    def print_sorted(self):
        """ This method prints the sorted list """
        sorted_list = list(self)
        sorted_list.sort()
        print(sorted_list)
