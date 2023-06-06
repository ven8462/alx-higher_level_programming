#!/usr/bin/python3

# Nested loop to generate combinations of two digits
for i in range(10):
    for j in range(i + 1, 10):
        # If !last combo, print the number with two digits, followed by a comma
        if j < 9 or (j == 9 and i < 8):
            print("{:d}{:d},".format(i, j), end="")
        # If last combo, print the number, followed by a newline
        elif j == 9 and i == 8:
            print("{:d}{:d}".format(i, j))
        # Add a space after each combination except the last one
        if j < 9 or (j == 9 and i < 8):
            print(" ", end="")
