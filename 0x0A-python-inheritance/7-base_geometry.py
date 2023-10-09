#!/usr/bin/python3
"""
Defining the class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Method to raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to raise Exception"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
