#!/usr/bin/python3
"""Module for no_c"""


def no_c(my_string):
    """Removes all characters c and C from a string"""
    return "".join([i for i in my_string if i != "c" and i != "C"])
