#!/usr/bin/python3
"""Unit tests for Rectangle."""
import io
import sys
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

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, "a")

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 0)

    def test_height_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, "a")

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2, 0, "a")

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_large(self):
        self.assertEqual(Rectangle(10, 7).area(), 70)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_default_x_y(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, height=2, x=3, y=4, id=99)
        self.assertEqual(r.id, 99)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_args_partial(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 10)

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d["width"], 10)

    def test_to_dictionary_full(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        expected = {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(d, expected)

    def test_display(self):
        r = Rectangle(2, 2, 0, 0)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        r = Rectangle(1, 1, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n #\n")


if __name__ == "__main__":
    unittest.main()
