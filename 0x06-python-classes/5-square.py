#!/usr/bin/python3
"""
Square Module
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side in square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))
