#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student instance.

        Args:
            attrs (list): optional list of attribute names to retrieve.
                If not a list of strings, all attributes are retrieved.
        """
        if isinstance(attrs, list):
            if all(isinstance(a, str) for a in attrs):
                return {k: v for k, v in self.__dict__.items()
                        if k in attrs}
        return self.__dict__
