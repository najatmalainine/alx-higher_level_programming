#!/usr/bin/python3
"""
Unittest for the Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_square.py
"""

import json
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Base Class"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_attr(self):
        """Testing the given attributes"""
        s = Square(10, 5, 6, 12)
        self.assertTrue(s.width == 10)
        self.assertTrue(s.height == 10)
        self.assertTrue(s.size == 10)
        self.assertTrue(s.x == 5)
        self.assertTrue(s.y == 6)
        self.assertTrue(s.id == 12)

    def test_attr_not_given(self):
        """Testing default attributes when not given"""
        s = Square(10, 2)
        self.assertTrue(s.width == 10)
        self.assertTrue(s.height == 10)
        self.assertTrue(s.size == 10)
        self.assertTrue(s.x == 2)
        self.assertTrue(s.y == 0)
        self.assertTrue(s.id is not None)

    def test_attr_errors(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([10], 2, 0, 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10, 2, 0, 12)

    def test_private_attr_access(self):
        """Test the accessibility for private attributes"""
        with self.assertRaises(AttributeError):
            print(Square.__width)
            print(Square.__x)
            print(Square.__y)

    def test_args(self):
        """Testing Too many and Too littel args"""
        with self.assertRaises(TypeError):
            Square(10, 2, 0, 0, 5, 6, 7)
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_class(self):
        """Test class created is Square"""
        self.assertEqual(type(Square(1, 2)), Square)

    def test_area(self):
        """Testing the area function"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(4, 0, 0).area(), 16)

    def test_display(self):
        """Test the display func"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(4).display()
            b = bufr.getvalue()
        self.assertEqual(b, '####\n####\n####\n####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Square(3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')

    def test_str(self):
        """Testing the __str__ method"""
        s = Square(3, 1, 3, 6)
        self.assertEqual(str(s), "[Square] (6) 1/3 - 3")

    def test_update(self):
        """Testing the update method"""
        s = Square(4, 6, 2, 12)
        """Test with *args"""
        s.update()
        self.assertEqual(str(s), "[Square] (12) 6/2 - 4")
        s.update(999)
        self.assertEqual(str(s), "[Square] (999) 6/2 - 4")
        s.update(999, 40)
        self.assertEqual(str(s), "[Square] (999) 6/2 - 40")
        s.update(999, 40, 60, 70)
        self.assertEqual(str(s), "[Square] (999) 60/70 - 40")
        """Test with **kwargs"""
        s.update(id=22)
        self.assertEqual(str(s), "[Square] (22) 60/70 - 40")
        s.update(id=22, x=77, y=88, size=99)
        self.assertEqual(str(s), "[Square] (22) 77/88 - 99")
        s.update(key=22, x=77, y=88, size=99)
        self.assertEqual(str(s), "[Square] (22) 77/88 - 99")

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        s_dict = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(s_dict), dict)
        s = Square(10, 10)
        s.update(**s_dict)
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')
