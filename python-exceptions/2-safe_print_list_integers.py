#!/usr/bin/python3
"""Module that safely prints and counts integers in a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integer elements of a list.

    Args:
        my_list (list): The list to process.
        x (int): The number of elements to access.

    Returns:
        int: The number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
