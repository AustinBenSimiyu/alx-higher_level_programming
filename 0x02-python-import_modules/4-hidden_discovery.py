#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":

    The_list = dir(hidden_4)
    Another_list = []
    for i in range(len(The_list)):
        if The_list[i][0] != "_" and The_list[i][1] != "_":
            Another_list.append(The_list[i])
        Another_list.sort()
    for i in range(len(Another_list)):
        print(Another_list[i])
