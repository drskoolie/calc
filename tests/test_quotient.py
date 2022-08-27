import pytest
from calculator.quotient import quotient

def test_quotient_simple():
    assert quotient(7, 3) == 1

def test_quotient_none():
    assert quotient(5, 6) == 5
