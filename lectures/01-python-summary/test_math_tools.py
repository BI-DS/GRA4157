import pytest


def is_even(x):
    if x%2==0:
        return True
    else:
        return False
        


def test_is_even():
    assert is_even(2) == True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#@pytest.mark.parametrize("x, expected", [(1,False),(2,True),(3, False),(5, False),(8, True)])
