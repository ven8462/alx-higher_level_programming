#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    arg_count = len(argv) - 1

    if arg_count == 0:
        print("{} arguments.".format(arg_count))
    elif arg_count == 1:
        print("{} argument:".format(arg_count))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(arg_count))
        for idx, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(idx, arg))
