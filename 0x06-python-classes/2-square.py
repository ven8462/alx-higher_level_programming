#!/usr/bin/python3

"""defines a class square with attributes"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0):
        """Initializes the square with size.
        Args:
        size(int, optional): Size of the square is 0.
        Raises:
            TypeError: If size is not int.
            ValueError: If size is less than 0.
        """

        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size most be >= 0")
        else:
            self.__size = size
