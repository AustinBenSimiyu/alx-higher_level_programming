#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Another_list = []
    for i in matrix:
        my_list = []
        for j in i:
            my_list.append(j**2)
        Another_list.append(my_list)
    return Another_list
