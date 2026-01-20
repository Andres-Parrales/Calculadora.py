# test_calculator.py

import pytest 
from calculator_core import add, divide
from errors import DivisionByZeroError


def test_add():
    assert add(5, 3) == 8


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)



