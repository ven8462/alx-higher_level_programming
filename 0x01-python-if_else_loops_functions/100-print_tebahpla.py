#!/usr/bin/python3

for char in range(122, 96, -1):
    if char % 2 == 0:
        i = char
    else:
        i = char - 32
    print("{}".format(char(i)), end='')
