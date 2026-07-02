#!/usr/bin/python3
"""Module for multiple_returns"""


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first
    character
    """
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
