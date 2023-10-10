#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class representing student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if isinstance(json, dict):
            for attr_name, value in json.items():
                if hasattr(self, attr_name):
                    setattr(self, attr_name, value)
