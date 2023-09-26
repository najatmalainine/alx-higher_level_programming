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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2 \
                and not all(isinstance(x, int) and x > 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                if self.__position[1] > 0:
                    print(" " * self.__position[1], end="")
                print("#" * self.size)
