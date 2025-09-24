# test_math_tools.py
import pytest

# Import the function to be tested
from math_tools import absolute_value, is_even

# py.test will automatically run functions starting with test_


@pytest.mark.parametrize(
    "x, expected_value", [(-3, 3), (1, 1), (0, 0), (10, 10), (-200, 200)]
)
def test_verify_absolute_func(x, expected_value):
    assert absolute_value(x) == expected_value
