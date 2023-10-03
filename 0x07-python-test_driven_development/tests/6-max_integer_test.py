#!/usr/bin/python3
"""Module to test the ``max_integer`` function from ``6-max_integer_test``
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Provides a method that uses unittest to
    test a function.
    """
    def test_positive_numbers(self):
        """Tests the max_integer function.

        Compares the output provided by the function
        with the expected output when list of positive
        integers is provided.
        """
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """
        tests the output when an empty list is provided.
        """
        self.assertIsNone(max_integer([]))

    def test_more_pos_ints(self):
        """
        Tests the output when more positive integers are porvided.
        """
        self.assertEqual(max_integer([3, 1, 4, 1, 5, 9, 2, 6, 5]), 9)

    def test_floats(self):
        """
        Tests the output when floats are provided.
        """
        self.assertEqual(max_integer([3.5, 1.2, 4.7, 2.8]), 4.7)

    def test_negative_numbers(self):
        """
        Tests negative numbers
        """
        self.assertEqual(max_integer([-3, -1, -4, -1, -5, -9, -2, -6, -5]), -1)

    def test_single_element_list(self):
        """
        Tests a single element list.
        """
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_numbers(self):
        """
        Tests duplicates.
        """
        self.assertEqual(max_integer([42, 42, 42]), 42)

    def test_positive_and_negative_numbers(self):
        """
        Tests a mixture of positive and negative numbers.
        """
        self.assertEqual(max_integer([-3, 1, -4, 1, -5, 9, -2, 6, -5]), 9)
