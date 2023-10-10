#!/usr/bin/python3
"""func that adds all arguments to a Python list,
and then save them to a file"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    old_data = load_from_json_file(filename)
except Exception:
    old_data = []

save_to_json_file(old_data + argv[1:], filename)
