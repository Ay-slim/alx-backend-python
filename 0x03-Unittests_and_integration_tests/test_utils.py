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
