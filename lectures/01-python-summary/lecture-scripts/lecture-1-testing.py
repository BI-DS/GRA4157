#!/usr/bin/env python3

# Python Testing with unittest


# Let's start with a simple function that needs testing:
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Now, let's write tests for this function:

import unittest


class TestAddFunction(unittest.TestCase):
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        """Test adding a positive number and a negative number."""
        self.assertEqual(add(2, -3), -1)


# If this script is run directly, run the tests:
if __name__ == "__main__":
    unittest.main()
