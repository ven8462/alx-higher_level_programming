#!/usr/bin/python3
""" Read from a file"""


def read_file(filename=""):
    """ Reads text froma file and prints to stdout"""
    with open(filename) as file:
        for line in file:
            print(line.strip())
