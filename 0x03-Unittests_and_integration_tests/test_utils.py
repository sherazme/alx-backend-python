#!/usr/bin/env python3
""" Tests for utils.py """
import unittest
from parameterized import parameterized
from typing import (
    Dict, Tuple, Union
)
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ method to test nested map access """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Dict,
            path: Tuple[str], expected: Union[int, Dict]
            ) -> None:
        """ Test access to nested map """
        self.assertEqual(
            expected,
            access_nested_map(nested_map, path)
        )

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict, path: Tuple[str]
            ) -> None:
        """ Test if an exception is raised correctly """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """  tests for get_json utility"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """ Test whether it returns valid json payload """
        config = {'return_value.json.return_value': test_payload}
        with patch('requests.get', autospec=True, **config) as mockRequestGet:
            self.assertEqual(get_json(test_url), test_payload)
            mockRequestGet.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ test for memoize utility function """
    def test_memoize(self) -> None:
        """ Test memoize function """
        class TestClass:
            """ Test class """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mockMethod:
            test = TestClass()
            self.assertEqual(test.a_property, mockMethod.return_value)
            self.assertEqual(test.a_property, mockMethod.return_value)
            mockMethod.assert_called_once()
