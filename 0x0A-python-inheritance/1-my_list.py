#!/usr/bin/python3
"""Module for MyList"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """Method for printing sorted list"""
        print(sorted(self))
