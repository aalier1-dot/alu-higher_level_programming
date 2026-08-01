#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    # --- basic instantiation ---

    def test_width_height(self):
        """width and height are set correctly."""
        r = Rectangle(3, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(3, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_x_y_given(self):
        """x and y can be given explicitly."""
        r = Rectangle(3, 5, 1, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_id_inherited(self):
        """Rectangle uses Base's id mechanism."""
        r1 = Rectangle(3, 5)
        r2 = Rectangle(3, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_id_given(self):
        """Rectangle accepts an explicit id."""
        r = Rectangle(3, 5, 1, 2, 99)
        self.assertEqual(r.id, 99)

    def test_is_base_instance(self):
        """Rectangle instances are also Base instances."""
        r = Rectangle(3, 5)
        self.assertIsInstance(r, 