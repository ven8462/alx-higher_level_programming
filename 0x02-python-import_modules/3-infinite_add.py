#!/bin/usr/python3

import sys

if __name__ == '__main__':

    for args in sys.argv[1:]:
        total_sum += int(args)

    print("{:d}".format(total_sum))
