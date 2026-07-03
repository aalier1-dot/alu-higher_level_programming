#!/usr/bin/python3
"""Module that divides two integers safely."""


def safe_print_division(a, b):
    """Divide a by b and print the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float: The result of the division, or None if it fails.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
