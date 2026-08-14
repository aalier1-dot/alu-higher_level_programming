#!/usr/bin/python3
"""Defines the Base model class."""
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV file <Class name>.csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            writer = csv.writer(f)
            if list_objs is None:
                list_objs = []
            for obj in list_objs:
                d = obj.to_dictionary()
                writer.writerow([d[field] for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes list of instances from <Class name>.csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                reader = csv.reader(f)
                list_dicts = [
                    {field: int(val) for field, val in zip(fields, row)}
                    for row in reader
                ]
                return [cls(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
