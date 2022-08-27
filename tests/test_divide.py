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


def test_divide_zero_first_arg():
    assert divide(0, 5) == 0


def test_divide_zero_second_arg():
    answer = divide(5, 0)
    assert answer != answer


def test_divide_zero_both_arg():
    answer = divide(0, 0)
    assert answer != answer
