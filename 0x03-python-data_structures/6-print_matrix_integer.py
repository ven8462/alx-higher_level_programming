#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = ["{:d}".format(val) for val in row]
        print(" ".join(formatted_row))
