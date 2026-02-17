# lesson12_tests/test_math_utils.py
import pytest
from src.utils.math_utils import add, percentage, avg

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
    ]
)
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize(
    "value,percent,expected",
    [
        (200, 10, 20),
        (50, 50, 25),
        (100, 0, 0)
    ]
)
def test_percentage(value, percent, expected):
    assert percentage(value, percent) == expected

def test_avg_normal():
    assert avg([1, 2, 3]) == 2

def test_avg_empty():
    with pytest.raises(ValueError):
        avg([])
