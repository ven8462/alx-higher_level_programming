#!/usr/bin/python3

def uppercase(str):
    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            c = chr(ord(n) - 32)
        else:
            c = n
        print("{}".format(c), end="")
    print()
