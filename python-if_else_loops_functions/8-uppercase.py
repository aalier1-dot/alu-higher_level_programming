#!/usr/bin/python3
def uppercase(str):
    """Print string in uppercase"""
    s = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            s += "{}".format(chr(ord(c) - 32))
        else:
            s += "{}".format(c)
    print("{}".format(s))
