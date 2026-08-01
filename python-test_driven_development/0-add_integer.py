#!/usr/bin/python3
"""Module that adds 2 integers.

This module provides a function to add two integers or floats.
It validates input types and casts floats to integers before adding.
"""


def add_integer(a, b=98):
    """Adds two integers or floats, returns integer.

    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
