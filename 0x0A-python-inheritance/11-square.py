#!/usr/bin/python3
"""
Defining the class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass Representing a Square"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """String representation method"""
        return (f"[Square] {self.__size}/{self.__size}")
