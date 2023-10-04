#!/usr/bin/python3
def islower(c):
    for number in range(97, 122):
        if number == ord(c):
            return True
    else:
        return False
