#!/usr/bin/python3
"""
Defining the class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass Representing a Rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
