#!/usr/bin/python3
for number in range(90):
    if number % 10 > number / 10:
        if number == 89:
            break
        print("{:02d}, ".format(number), end="")
print("89")
