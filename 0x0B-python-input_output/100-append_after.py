#!/usr/bin/python3
"""a function that inserts a line of text to a file,
after each line containing a specific string"""


def insert_line_after_string(filename, search_string, new_line):
    """inserts a line of text to a file"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if search_string in line:
            lines.insert(i + 1, new_line + '\n')
            break

    with open(filename, 'w') as file:
        file.writelines(lines)
