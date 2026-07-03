#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print value as an integer if possible.

    Args:
        value: The value to print.

    Returns:
        bool: True if value was printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
