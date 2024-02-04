#!/usr/bin/env python3
"""Module containing function tests"""


import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """Class containing acess nested tests"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, n_dict: Mapping,
                               path: Sequence, result: Any) -> None:
        """Function to test nested map function"""
        self.assertEqual(access_nested_map(n_dict, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, n_dict: Mapping,
                                         path: Sequence) -> None:
        """Function to test nested map function error"""
        with self.assertRaises(KeyError):
            access_nested_map(n_dict, path)
