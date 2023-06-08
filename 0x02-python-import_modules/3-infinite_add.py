#!/bin/usr/python3

if __name__ == '__main__':
    from sys import argv

    sum = 0
    for args in argv[1:]:
        sum += int(args)

    print(sum)
