#!/usr/bin/python3
"""Unit tests for Rectangle."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_width_height(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_is_base_instance(self):
        r = Rectangle(3, 5)
        self.assertIsInstance(r, Base)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("a", 2)

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, "a")

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "a")

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 0, "a")

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d["width"], 10)


if __name__ == "__main__":
    unittest.main()
