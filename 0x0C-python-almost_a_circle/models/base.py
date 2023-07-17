#!/usr/bin/python3
"""base class"""


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class"""
        if id is not None:
            self.id = id
        else:
            __class__.__nb_objects += 1
            self.id = __class__.__nb_objects
