import pytest


def is_even(x):
    if x%2==0:
        return True
    else:
        return False
        
        
@pytest.mark.parametrize("x, expected", [(1,False),(2,True),(3, False),(5, False),(8, True)])

def test_is_even(x, expected):
    assert is_even(x) == expected
