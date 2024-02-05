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

    def test_public_repos_url(self) -> None:
        """Public repos url test"""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as sample_org:
            sample_org.return_value = {"repos_url": "test"}
            testClass = GithubOrgClient("test")
            self.assertEqual(testClass._public_repos_url, "test")
