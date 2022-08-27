import pytest
from calculator.multiply import multiply


def test_multiply_simple():
    assert multiply(3, 5) == 15


def test_multiply_negative_first_arg():
    assert multiply(-3, 5) == -15


def test_multiply_negative_second_arg():
    assert multiply(3, -5) == -15


def test_multiply_zero_first_arg():
    assert multiply(0, 5) == 0


def test_multiply_zero_second_arg():
    assert multiply(5, 0) == 0
