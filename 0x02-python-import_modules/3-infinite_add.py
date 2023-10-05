#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num = 0
    if (len(sys.argv) - 1) > 0:
        for i in range(1, len(sys.argv)):
            num += int(sys.argv[i])
        print("{}".format(num))
    else:
        print("{}".format(num))
