#!/usr/bin/python3
"""define a square class"""


class Square:
    def __init__(self, size=0):
        """Initializes the square with size.

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area
        """
        return self.__size * self.__size
