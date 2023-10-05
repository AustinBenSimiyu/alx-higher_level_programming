#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args > 1:
        print("{} arguments".format(num_args))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
    elif num_args == 1:
        print("{} argument".format(num_args))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments".format(num_args))
