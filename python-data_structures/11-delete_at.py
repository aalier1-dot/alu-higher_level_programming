#!/usr/bin/python3
"""Module for delete_at"""


def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    return my_list[:idx] + my_list[idx + 1:]
