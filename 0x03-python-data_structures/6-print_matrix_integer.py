#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if num != 0:
                print("", end="")
            print("{:d}".format(num), end="")
        print()
