import pytest
from calculator.divide import divide

def test_divide_simple():
    assert divide(10, 5) == 2

def test_divide_negative_first_arg():
    assert divide(10, -5) == -2

def test_divide_negative_second_arg():
    assert divide(-10, 5) == -2

def test_divide_negative_both_arg():
    assert divide(-10, -5) == 2
