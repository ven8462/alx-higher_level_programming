#!/usr/bin/python3

"""prints a square"""


class Square:
    """Defines a square.
    """
    def __init__(self, size=0):
        """Initializes the square."""
        self.size = size

    @property
    def size(self):
        """Gets the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the '#' character.
        """
        if self.__size == 0:
            print()
        else:
            print('\n'.join('#' * self.__size for _ in range(self.__size)))
