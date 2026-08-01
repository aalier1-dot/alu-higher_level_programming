#!/usr/bin/python3
"""
This module contains the function print_square(size).
It prints a square of size `size` using the `#` character.
"""


def print_square(size):
    """
    Prints a square with the character `#`.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
