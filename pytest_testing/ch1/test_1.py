import pytest


def test_passing():
    assert (1,2,3) == (1,2,3)
    
@pytest.mark.xfail
def test_not_passing():
    assert (3,2,1) == (1,2,3)

    
def test_riase():
    raise TypeError()