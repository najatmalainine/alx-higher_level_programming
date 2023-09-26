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
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size
