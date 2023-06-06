#!/usr/bin/python3

# Loop through numbers from 0 to 99
for i in range(100):
    # print the number with two digits, followed by a comma and space
    if i < 99:
        print("{:02d}, ".format(i), end="")
    # If it's the last number, print the number with two digits and a newline
    else:
        print("{:02d}".format(i))
