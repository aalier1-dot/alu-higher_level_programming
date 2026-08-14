#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_is_none(self):
        """When no id is given, id is set from the counter."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_increments(self):
        """Each new instance without an id increments counter."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_given(self):
        """When an id is given, it is used as is."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_given_does_not_increment_counter(self):
        """Giving an explicit id should not affect the counter."""
        b1 = Base(50)
        b2 = Base()
        self.assertEqual(b1.id, 50)
        self.assertEqual(b2.id, 1)

    def test_id_none_explicit(self):
        """Explicitly passing id=None behaves like no id given."""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_id_zero(self):
        """An id of 0 is a valid explicit id."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """A negative id is accepted as given."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_string(self):
        """A string id is accepted as given."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_no_args_instantiation(self):
        """Base() with no arguments should not raise."""
        try:
            Base()
        except Exception as e:
            self.fail("Base() raised an exception: {}".format(e))

    def test_save_to_file_csv_empty_list(self):
        """save_to_file_csv with empty list creates empty file."""
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "")
        os.remove("Rectangle.csv")

    def test_save_to_file_csv_none(self):
        """save_to_file_csv with None behaves like empty list."""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            content = f.read()
        self.assertEqual(content, "")
        os.remove("Rectangle.csv")

    def test_load_from_file_csv_no_file(self):
        """load_from_file_csv returns [] if file is missing."""
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")
        result = Square.load_from_file_csv()
        self.assertEqual(result, [])

    def test_save_and_load_rectangle_csv(self):
        """Rectangle CSV round-trip preserves attributes."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        result = Rectangle.load_from_file_csv()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(result[1].to_dictionary(), r2.to_dictionary())
        os.remove("Rectangle.csv")

    def test_save_and_load_square_csv(self):
        """Square CSV round-trip preserves attributes."""
        s1 = Square(5, 0, 0, 5)
        s2 = Square(7, 9, 1, 6)
        Square.save_to_file_csv([s1, s2])
        result = Square.load_from_file_csv()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(result[1].to_dictionary(), s2.to_dictionary())
        os.remove("Square.csv")

    def test_to_json_string_none(self):
        """to_json_string(None) returns \"[]\"."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """to_json_string([]) returns \"[]\"."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """to_json_string returns valid JSON for a list of dicts."""
        result = Base.to_json_string([{"id": 12}])
        self.assertEqual(result, "[{\"id\": 12}]")

    def test_from_json_string_none(self):
        """from_json_string(None) returns []."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """from_json_string(\"\") returns []."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """from_json_string parses back to the original list."""
        result = Base.from_json_string("[{\"id\": 12}]")
        self.assertEqual(result, [{"id": 12}])

    def test_json_round_trip(self):
        """to_json_string and from_json_string are inverses."""
        original = [{"id": 1}, {"id": 2}]
        s = Base.to_json_string(original)
        self.assertEqual(Base.from_json_string(s), original)

    def test_save_to_file_none(self):
        """save_to_file(None) writes an empty-list JSON file."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")
        os.remove("Rectangle.json")

    def test_save_and_load_rectangle_json(self):
        """Rectangle JSON round-trip preserves attributes."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(result[1].to_dictionary(), r2.to_dictionary())
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """load_from_file returns [] if the file is missing."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_create_partial_id(self):
        """create with only id sets id, keeps default other attrs."""
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(r.id, 89)

    def test_create_partial_id_width(self):
        """create with id and width sets both correctly."""
        r = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_create_partial_id_width_height(self):
        """create with id, width, height sets all three."""
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_create_partial_id_width_height_x(self):
        """create with id, width, height, x sets all four."""
        d = {"id": 89, "width": 1, "height": 2, "x": 3}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.x, 3)

    def test_create_full_rectangle(self):
        """create with all attributes sets every field."""
        d = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        r = Rectangle.create(**d)
        self.assertEqual(r.to_dictionary(), d)

    def test_create_square(self):
        """create works for Square with size."""
        s = Square.create(**{"id": 5, "size": 2})
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 2)


if __name__ == '__main__':
    unittest.main()
