#!/usr/bin/python3
"""Module for print_reversed_list_integer"""


def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order"""
    for number in my_list[::-1]:
        print("{:d}".format(number))
