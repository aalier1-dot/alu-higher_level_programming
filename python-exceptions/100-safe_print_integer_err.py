#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer.

    Returns:
        True if value is an integer.
        False otherwise and prints the exception to stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
