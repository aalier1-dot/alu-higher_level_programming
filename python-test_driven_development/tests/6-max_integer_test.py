#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_max_at_end(self):
        """max is the last element"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """max is somewhere in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_start(self):
        """max is the first element"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_single_element(self):
        """list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """empty list returns None"""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """default argument (no list given) returns None"""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """list with only negative numbers"""
        self.assertEqual(max_integer([-5, -1, -10, -3]), -1)

    def test_mixed_positive_negative(self):
        """list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-5, 3, -1, 0, 2]), 3)

    def test_all_same_values(self):
        """all elements are equal"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_two_elements(self):
        """list with exactly two elements"""
        self.assertEqual(max_integer([2, 10]), 10)
        self.assertEqual(max_integer([10, 2]), 10)

    def test_return_type(self):
        """return value keeps the type of the max element"""
        self.assertIsInstance(max_integer([1, 2, 3]), int)


if __name__ == '__main__':
    unittest.main()
