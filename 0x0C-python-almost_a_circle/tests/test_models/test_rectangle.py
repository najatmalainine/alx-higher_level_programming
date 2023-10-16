#!/usr/bin/python3
"""
Unittest for the Rectangle Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""

import json
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Base Class"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_attr(self):
        """Testing the given attributes"""
        r = Rectangle(10, 2, 5, 6, 12)
        self.assertTrue(r.width == 10)
        self.assertTrue(r.height == 2)
        self.assertTrue(r.x == 5)
        self.assertTrue(r.y == 6)
        self.assertTrue(r.id == 12)

    def test_attr_not_given(self):
        """Testing default attributes when not given"""
        r = Rectangle(10, 2)
        self.assertTrue(r.width == 10)
        self.assertTrue(r.height == 2)
        self.assertTrue(r.x == 0)
        self.assertTrue(r.y == 0)
        self.assertTrue(r.id is not None)

    def test_attr_errors(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([10], 2, 0, 0, 12)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2", 0, 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None, 0, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, (1, 2), 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2, 0, 0, 12)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0, 0, 0, 12)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -6, 0, 12)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -4, 12)

    def test_private_attr_access(self):
        """Test the accessibility for private attributes"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_args(self):
        """Testing Too many and Too littel args"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 5, 6, 7)
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    def test_class(self):
        """Test class created is Rectangle"""
        self.assertEqual(type(Rectangle(1, 2)), Rectangle)

    def test_area(self):
        """Testing the area function"""
        self.assertEqual(Rectangle(10, 2).area(), 20)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).area(), 20)

    def test_display(self):
        """Test the display func"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_str(self):
        """Testing the __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Testing the update method"""
        r = Rectangle(4, 6, 2, 1, 12)
        """Test with *args"""
        r.update()
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")
        r.update(999)
        self.assertEqual(str(r), "[Rectangle] (999) 2/1 - 4/6")
        r.update(999, 40)
        self.assertEqual(str(r), "[Rectangle] (999) 2/1 - 40/6")
        r.update(999, 40, 60)
        self.assertEqual(str(r), "[Rectangle] (999) 2/1 - 40/60")
        r.update(999, 40, 60, 20)
        self.assertEqual(str(r), "[Rectangle] (999) 20/1 - 40/60")
        r.update(999, 40, 60, 20, 10)
        self.assertEqual(str(r), "[Rectangle] (999) 20/10 - 40/60")
        """Test with **kwargs"""
        r.update(id=22)
        self.assertEqual(str(r), "[Rectangle] (22) 20/10 - 40/60")
        r.update(id=22, x=77, y=88, width=99, height=66)
        self.assertEqual(str(r), "[Rectangle] (22) 77/88 - 99/66")

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        r_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(r_dict), dict)
        r = Rectangle(10, 10)
        r.update(**r_dict)
        self.assertEqual(str(r), '[Rectangle] (5) 3/4 - 1/2')
