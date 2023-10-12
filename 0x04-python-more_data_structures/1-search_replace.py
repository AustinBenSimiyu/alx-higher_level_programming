#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    new_list = my_list.copy()
    for element in new_list:
        if element == search:
            num = new_list.index(element)
            new_list[num] = replace
    return new_list
