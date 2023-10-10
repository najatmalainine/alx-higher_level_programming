#!/usr/bin/python3
"""The desterialization (from a “JSON file”) func"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, mode="r", encoding="utf-8") as f:
        json.load(f)
