#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A test suite for the max_integer function."""

    def test_empty_list(self) -> None:
        """Test when given an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_no_arg(self) -> None:
        """Test when no argument is provided."""
        self.assertEqual(max_integer(), None)

    def test_sorted_list(self) -> None:
        """Test when given a sorted list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 7]), 7)

    def test_unsorted_list(self) -> None:
        """Test when given an unsorted list of integers."""
        self.assertEqual(max_integer([2, 8, 9, 2, 1]), 9)

    def test_max_first_lis(self) -> None:
        """Test when Max number is at beginning."""
        self.assertEqual(max_integer([8, 5, 1]), 8)

    def test_only_one(self) -> None:
        """Test when there's only one element in the list."""
        self.assertEqual(max_integer([8]), 8)

    def test_float_list(self) -> None:
        """Text when given a list of float number."""
        self.assertEqual(max_integer([1.5, 4.5, 0.2]), 4.5)

    def test_mix_nbr_list(self) -> None:
        """Test when given a list of mixed numeric types."""
        self.assertEqual(max_integer([1.05, 4.5, 8, 7.9, 7, 4]), 8)

    def test_nigative_int_list(self) -> None:
        """Text when given a list with nigative numbers."""
        self.assertEqual(max_integer([-4, -5, -1, -9]), -1)

    def test_empty_string(self) -> None:
        """Test when an empty string is provided."""
        self.assertEqual(max_integer(""), None)

    def test_str_list(self) -> None:
        """Test when given a list of strings."""
        self.assertEqual(max_integer(["a9bc", "abc7", "1abc"]), "abc7")
