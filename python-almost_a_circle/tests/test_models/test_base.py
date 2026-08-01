#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
from models.base import Base


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
        """Each new instance without an id increments the counter."""
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
        """An id of 0 is a valid explicit id (not treated as falsy)."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """A negative id is accepted as given."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_string(self):
        """A string id is accepted as given (Base does not validate)."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_no_args_instantiation(self):
        """Base() with no arguments should not raise an error."""
        try:
            Base()
        except Exception as e:
            self.fail("Base() raised an exception: {}".format(e))


if __name__ == '__main__':
    unittest.main()
