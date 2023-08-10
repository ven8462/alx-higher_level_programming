#!/usr/bin/python3

import sys
import unittest
import inspect
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    class for testing Rectangle class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Rectangle, inspect.isfunction)

    def setUp(self):
        self.rec_one = Rectangle(1,1,1,1)

    def test_create_instance(self):
        print()
        print(self.rec_one)
        self.assertIsInstance(self.rec_one, Rectangle)

    def test_float_width(self):
        with self.assertRaises(TypeError):
            Rectangle(1.12, 1, 1, 1)