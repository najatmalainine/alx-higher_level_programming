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

    def area(self):
        """Method for calculating the area"""
        return self.__width * self.__height

    def __str__(self):
        """String representation method"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
