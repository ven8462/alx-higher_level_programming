#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """ define a class with with width and height attributes"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """gets the width"""
            return self.__width

        @width.setter
        def width(self, value):
            """sets width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

            @property
            def height(self):
                """gets the height"""
                return self.__height

            @height.setter
            def height(self, value):
                """sets height"""
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                elif value < 0:
                    raise ValueError("height must be >= 0")
                else:
                    self.__height = value
                    raisa
