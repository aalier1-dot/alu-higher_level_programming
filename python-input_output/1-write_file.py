#!/usr/bin/python3
"""Module that writes a string to a text file (UTF8)."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8), creating/overwriting it.

    Args:
        filename: the name of the file to write to.
        text: the string to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
