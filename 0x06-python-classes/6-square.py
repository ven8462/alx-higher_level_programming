#!/usr/bin/python3

"""define a square class"""


class Square:
    """Defines a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with an optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size ensuring it is a non-negative integer."""
        # Size setter code remains the same

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position ensuring it is   2 non-negative integers."""
        # if it is write code raise an exception

    def area(self):
        """Calculates and returns the current square's area."""
        # Area code remains the same

    def my_print(self):
        """Prints the square considering its position."""
        # Update print method to consider position
