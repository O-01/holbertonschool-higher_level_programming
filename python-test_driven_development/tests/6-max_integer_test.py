#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittest for max_integer method """

    def test_type(self):
        """ tests to ensure verification of list data type """
        self.assertIs(list, list)
        self.assertRaises(TypeError, max_integer("Hi"))

    def test_empty(self):
        """ tests to verify None return upon empty list input """
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """ tests correct operation if list contains only one element """
        self.assertEqual(max_integer([12]), 12)

    def test_negative_one(self):
        """ tests correct operation if one list element is negative """
        self.assertEqual(max_integer([1, 2, -4, 8]), 8)

    def test_negative_all(self):
        """ tests correct operation if all list elements are negative """
        self.assertEqual(max_integer([-1, -2, -4, -8]), -1)

    def test_positive_one(self):
        """ tests correct operation if one list element is positive """
        self.assertEqual(max_integer([-1, -2, 4, -8]), 4)

    def test_positive_all(self):
        """ tests correct operation if all list elements are positive """
        self.assertEqual(max_integer([1, 2, 4, 8]), 8)

    def test_max_first(self):
        """ tests correct operation if first element is max """
        self.assertEqual(max_integer([256, 16, 32, 64, 128]), 256)

    def test_max_mid(self):
        """ tests correct operation if first element is max """
        self.assertEqual(max_integer([16, 32, 256, 64, 128]), 256)

    def test_max_last(self):
        """ tests correct operation if last element is max """
        self.assertEqual(max_integer([16, 32, 64, 128, 256]), 256)

    def test_excessive_arguments(self):
        """ tests to verify TypeError upon excessive argument input """
        with self.assertRaises(TypeError):
            max_integer([24, 48], 2)
            max_integer([24, 48], "Hi", 2)

    def test_none(self):
        """ tests to verify TypeError upon None input """
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
