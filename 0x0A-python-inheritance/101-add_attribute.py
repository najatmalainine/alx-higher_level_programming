#!/usr/bin/python3
"""
adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """
    adds new attribute if possible
    else raises error
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
