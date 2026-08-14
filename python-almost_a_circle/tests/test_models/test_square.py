#!/usr/bin/python3
"""Unit tests for Square."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        s = Square(5)
        self.assertEqual(s.width, 5)

    def test_is_rectangle_instance(self):
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_is_base_instance(self):
        s = Square(5)
        self.assertIsInstance(s, Base)

    def test_width_equals_height(self):
        s = Square(7)
        self.assertEqual(s.width, s.height)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_size(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_size_updates_width_and_height(self):
        s = Square(5)
        s.size = 8
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

    def test_size_type(self):
        with self.assertRaises(TypeError):
            Square("a")

    def test_size_value(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-3)

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_args(self):
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=9, x=1, y=2, id=7)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 9)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d["size"], 10)

    def test_to_dictionary_full(self):
        s = Square(10, 2, 1, 9)
        d = s.to_dictionary()
        expected = {"id": 9, "size": 10, "x": 2, "y": 1}
        self.assertEqual(d, expected)

    def test_display(self):
        s = Square(2, 0, 0)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")


if __name__ == "__main__":
    unittest.main()
