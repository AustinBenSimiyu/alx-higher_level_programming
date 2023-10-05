#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    num = (len(sys.argv) - 1)
    if num == 3:
        symbols = ["+", "-", "*", "/"]
        a = int(sys.argv[1])
        x = (sys.argv[2])
        b = int(sys.argv[3])
        if symbols[0] == x:
            print("{} {} {} = {}".format(a, symbols[0], b, add(a, b)))
        elif symbols[1] == x:
            print("{} {} {} = {}".format(a, symbols[1], b, sub(a, b)))
        elif symbols[2] == x:
            print("{} {} {} = {}".format(a, symbols[2], b, mul(a, b)))
        elif symbols[3] == x:
            print("{} {} {} = {}".format(a, symbols[3], b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
