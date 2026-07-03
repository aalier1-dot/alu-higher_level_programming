#!/usr/bin/python3
"""Module that prints a list of integers in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list, one per line, in reverse order.

    Args:
        my_list (list): The list of integers to print.
    """
    if my_list is None:
        return
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
