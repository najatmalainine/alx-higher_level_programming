#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

# ------- Another Method -----------
# def no_c(my_string):
# return ("".join(c for c in my_string if c not in "Cc"))
