#!/usr/bin/python3
"""Module for divisible_by_2"""


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    return [number % 2 == 0 for number in my_list]
