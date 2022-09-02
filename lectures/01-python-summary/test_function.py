import pytest


# define aboslute value
def f(x):
    if x < 0:
        return x
    else:
        return x
        

# test absolute value
@pytest.mark.parametrize("x, expected_value", [(-1,1), (2,2)])

def test_absolute_value_function(x, expected_value):
    assert f(x) == expected_value
    
