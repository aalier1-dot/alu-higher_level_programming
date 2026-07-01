#!/usr/bin/python3
"""Module for search_replace"""


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list"""
    return [replace if item == search else item for item in my_list]
