#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_first = tuple_a + (0, 0)
    sum_second = tuple_b + (0, 0)
    a = sum_first[0] + sum_second[0]
    b = sum_first[1] + sum_second[1]
    return (a, b)
