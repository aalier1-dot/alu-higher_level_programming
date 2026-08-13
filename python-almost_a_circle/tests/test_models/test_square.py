#!/usr/bin/python3
"""Unit tests for Square."""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        s = Square(5)
        self.assertEqual(s.width, 5)

    def test_size(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_size_type(self):
        with self.assertRaises(TypeError):
            Square("a")

    def test_size_value(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_args(self):
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d["size"], 10)


if __name__ == "__main__":
    unittest.main()
