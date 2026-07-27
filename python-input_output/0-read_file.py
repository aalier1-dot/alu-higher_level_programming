#!/usr/bin/python3
"""Module that reads a text file and prints its contents to stdout."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: the name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
