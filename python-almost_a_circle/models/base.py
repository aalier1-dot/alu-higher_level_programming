#!/usr/bin/python3
"""Defines the Base model class."""


class Base:
    """
    Base class for all other classes in this project.
    Manages the private __nb_objects attribute, used to assign a
    unique id to every new instance if no id is given.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int): the identity of the new instance. If None,
                the id is set using the incremented value of
                __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
