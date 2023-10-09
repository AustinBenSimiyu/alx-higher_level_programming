#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        max_int = None
    else:
        my_list.sort()
        my_list.reverse()
        max_int = my_list[0]
    return max_int
