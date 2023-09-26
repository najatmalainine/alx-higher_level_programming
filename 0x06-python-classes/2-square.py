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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
