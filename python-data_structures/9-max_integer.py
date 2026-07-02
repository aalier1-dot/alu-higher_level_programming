#!/usr/bin/python3
"""Module for max_integer"""


def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None
    biggest = my_list[0]
    for number in my_list:
        if number > biggest:
            biggest = number
    return biggest
