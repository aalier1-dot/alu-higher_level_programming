#!/usr/bin/python3
"""Module that deletes an item at a specific index in a list."""


def delete_at(my_list=[], idx=0):
    """Delete the item at the given index in the list.

    Args:
        my_list (list): The list to modify.
        idx (int): The index of the item to delete.

    Returns:
        list: The modified list.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
