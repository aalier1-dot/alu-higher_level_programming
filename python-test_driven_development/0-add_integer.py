#!/usr/bin/python3
"""
This module contains the function add_integer(a, b=98).
It adds a and b together after casting both to integers.
Raises TypeError if either is not an int or float.
"""


def add_integer(a, b=98):
    """
    Adds a and b, after first casting each to an int.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
