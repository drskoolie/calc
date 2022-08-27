import pytest
from calculator.core import add, sub


def test_add_simple():
    assert add(5, 3) == 8


def test_add_negative():
    assert add(5, -2) == 3


def test_sub_simple():
    assert sub(5, 3) == 2


def test_sub_negative():
    assert sub(5, -2) == 7
