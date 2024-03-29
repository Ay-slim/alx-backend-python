#!/usr/bin/env python3
"""Module containing function tests"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Dict, Mapping, Sequence, Any
from unittest.mock import Mock, patch


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


class TestGetJson(unittest.TestCase):
    """Class containing get json test"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict) -> None:
        """Function to test json_get"""
        with patch("requests.get", return_value=Mock(**{
                'json.return_value': test_payload})) as req_obj:
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            req_obj.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Class testing memoization"""

    def test_memoize(self) -> None:
        """Test the memoize decorator"""
        class TestClass:
            """A class to test memoization"""

            def a_method(self) -> int:
                """Return 42"""
                return 42

            @memoize
            def a_property(self) -> int:
                """Return the a_method"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as afunc:
            clsInstance = TestClass()
            clsInstance.a_property
            clsInstance.a_property
            afunc.assert_called_once
            self.assertEqual(clsInstance.a_property, afunc.return_value)
