#!/usr/bin/python3

# Initialize an empty string
alphabet = ""

# Loop through lowercase ASCII alphabet (ASCII values from 97 to 122)
for i in range(97, 123):
    # Skip 'q' and 'e'
    if i == 101 or i == 113:
        continue

    # Concatenate the character to the alphabet string
    alphabet += chr(i)

# Print the alphabet string without a newline
print("{}".format(alphabet), end="")
