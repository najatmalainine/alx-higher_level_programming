#!/usr/bin/python3
def isupper(c):
    if 'a' <= c <= 'z':
        return chr(ord(c) - 32)
    else:
        return c
