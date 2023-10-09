#!/usr/bin/python3
"""
Defining the class MyInt
"""


class MyInt(int):
    """Subclass MyInt"""
    def __init__(self, n):
        """Constructor"""
        self.n = n

    def __eq__(self, value):
        """Method for equality"""
        return int(self) != value

    def __ne__(self, value):
        """Method for non-equality"""
        return int(self) == value
