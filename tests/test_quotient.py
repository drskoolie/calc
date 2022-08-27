import pytest
from calculator.quotient import quotient

def test_quotient_simple():
    assert quotient(7, 3) == 1

def test_quotient_none():
    assert quotient(5, 6) == 5

def test_quotient_zero_first_arg():
    assert quotient(0, 10) == 0

def test_quotient_zero_second_arg():
    answer = quotient(10, 0)
    assert answer != answer

def test_quotient_zero_both_arg():
    answer = quotient(0, 0)
    assert answer != answer

def test_quotient_negative_first_arg():
    assert quotient(-10, 3) == -1

def test_quotient_negative_second_arg():
    assert quotient(10, -3) == -1

def test_quotient_negative_both_arg():
    assert quotient(-10, -3) == 1
