#!/usr/bin/python3
"""
This module contains the function text_indentation(text).
It prints text with two new lines after each ., ? and : character,
without any leading or trailing spaces on each printed line.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ., ? and : character.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False
    for char in text:
        if skip_space and char == " ":
            continue
        skip_space = False
        print(char, end="")
        if char in ".?:":
            print("\n")
            skip_space = True
