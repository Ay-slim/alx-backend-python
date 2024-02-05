#!/usr/bin/env python3
"""Module containing client tests"""


import unittest
from parameterized import parameterized
from client import GithubOrgClient
from typing import Callable
from unittest.mock import Mock, MagicMock, PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Class containing github org client tests"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org: str, methodToSimulate: Callable) -> None:
        """Function to test github org methods"""
        gitInstance = GithubOrgClient(org)
        gitInstance.org()
        methodToSimulate.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
