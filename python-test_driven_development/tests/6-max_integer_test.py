#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_repeated_max(self):
        """Test list with repeated maximum values"""
        self.assertEqual(max_integer([2, 4, 4, 1]), 4)

    def test_float_values(self):
        """Test list with float values"""
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    def test_string_list(self):
        """Test list of strings (lexicographic comparison)"""
        self.assertEqual(max_integer(["a", "z", "m"]), "z")


if __name__ == "__main__":
    unittest.main()
