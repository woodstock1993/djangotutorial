import pytest
pytest = pytest.mark.unit

def test_pass():
    assert 1 + 1 == 2

def test_fail():
    assert 2 + 2 == 4