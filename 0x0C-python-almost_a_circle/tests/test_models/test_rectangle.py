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