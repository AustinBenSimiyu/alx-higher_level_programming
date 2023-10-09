#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list) - 1):
        if my_list[i] % 2 == 0:
            new_list.insert(i, True)
        else:
            new_list.insert(i, False)
    return new_list
