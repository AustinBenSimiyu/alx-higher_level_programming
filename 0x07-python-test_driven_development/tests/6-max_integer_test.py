#!/usr/bin/python3
"""Unittest for max_integer([..]) function
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)
        self.assertEqual(max_integer([1.10, 2.20, 6.60, 4.2]), 6.60)
        self.assertEqual(max_integer([0, 0, 0, 0.000]), 0)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -22, -3.44, -4.111]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -0]), 0)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_no_args(self):
        self.assertEqual(max_integer(), None)
