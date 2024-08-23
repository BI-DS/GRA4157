# test_math_tools.py
import pytest
# Import the function to be tested
from math_tools import absolute_value

# py.test will automatically run functions starting with test_ 
def test_verify_absolute_func():         
    # Add some tests here...
    assert absolute_value(-3) == 3       
    assert absolute_value(5)  == 5       
    assert absolute_value(0)  == 0