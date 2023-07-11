#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename, search_string, new_string):
    """inserts a line of text to a file"""
    with open(filename, 'r') as file:
        text = file.readlines()

    with open(filename, 'w') as fw:
        string = ""
        for line in text:
            string += line
            if search_string in line:
                string += new_string
                fw.write(string)
