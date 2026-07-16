#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (float/int): The size of the new Square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check equality based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check inequality based on area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check greater-than based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check greater-or-equal based on area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check less-than based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check less-or-equal based on area."""
        return self.area() <= other.area()
