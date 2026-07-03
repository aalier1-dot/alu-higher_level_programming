#!/usr/bin/python3
"""Module that raises a name exception with a message."""


def raise_exception_msg(message=""):
    """Raise a NameError with the given message.

    Args:
        message (str): The message to attach to the exception.
    """
    raise NameError(message)
