#!/usr/bin/env python3
'''A module for testing the utils module'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize  # Import memoize


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class to test access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function with various inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("a", "b", "c")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test raises KeyError for invalid inputs."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class to test get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function with various inputs."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """TestMemoize class to test the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches method calls properly."""

        class TestClass:
            """A class to test memoization."""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

            with patch.object(TestClass, "a_method", return_value=42) 
            as mock_method:
            test_instance = TestClass()

            # First call to a_property (should call a_method)
            result1 = test_instance.a_property
            # Second call to a_property (should use cached value)
            result2 = test_instance.a_property

            # Ensure results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method is only called once
            mock_method.assert_called_once()
