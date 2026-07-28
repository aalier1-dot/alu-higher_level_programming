#!/usr/bin/python3
"""Defines a function that returns the dict description of an object."""


def class_to_json(obj):
    """Return the dictionary description of a simple-structure object.

    Args:
        obj: an instance of a Class with only serializable attributes
            (list, dict, str, int, bool).
    """
    return obj.__dict__
