#!/usr/bin/python3

"""define a square class"""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position ensuring it's a tuple of 2 non-ve integers."""
        if not isinstance(value, tuple) or len(value) != 2 or\
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current square's area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
