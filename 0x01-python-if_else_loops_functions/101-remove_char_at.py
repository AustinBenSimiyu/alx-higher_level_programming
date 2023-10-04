#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        new_str = str[:n] + str[n + 1:]
    else:
        new_str = str
    return (new_str)
