#!/usr/bin/python3
"""Module that adds a new attribute to an object, if possible."""
def add_attribute(obj, name, value):
    """Adds a new attribute to an object, raises TypeError if not possible.
    Args:
        obj: the object to add the attribute to.
        name: the name of the attribute.
        value: the value of the attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
