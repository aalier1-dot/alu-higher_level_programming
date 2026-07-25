#!/usr/bin/python3
"""Defines a MyInt class that inverts == and != from int."""


class MyInt(int):
    """Represent an integer with inverted == and != operators."""

    def __eq__(self, other):
        """Return the inverted equality comparison."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return the inverted inequality comparison."""
        return super().__eq__(other)
