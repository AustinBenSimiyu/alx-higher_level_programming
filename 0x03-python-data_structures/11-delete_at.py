#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list.extend(my_list[:idx])
        new_list.extend(my_list[idx + 1:])
        my_list.clear()
        my_list.extend(new_list)
        return my_list
