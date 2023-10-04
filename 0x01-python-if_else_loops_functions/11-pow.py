#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b < 0:
        b = b * -1
        x = 1
    else:
        x = 0
    for i in range(b):
        c = a * c
    if x == 1:
        c = (1 / c)
    return c
