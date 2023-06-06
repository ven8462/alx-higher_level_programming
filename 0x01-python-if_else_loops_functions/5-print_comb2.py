#!/usr/bin/python3

# Loop through numbers from 0 to 99
for i in range(100):
    # print the number with two digits, followed by a comma and space
    print("{:02d}, ".format(i) if i < 99 else "{:02d}\n".format(i), end="")
