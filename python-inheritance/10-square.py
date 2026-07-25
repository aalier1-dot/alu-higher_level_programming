#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int):quare.

        Args:
            size (int): The size of the new Square.
        """
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square."""
        return super().area()
