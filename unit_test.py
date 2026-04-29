import pytest
from calculator import Calculator

def test_successful_division():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0

def test_divide_by_zero_throws_exception():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)

def test_purchase_discount():
    calc = Calculator()
    input_price = 120.0
    expected_result = 108.0
    assert calc.calculate_total(input_price) == expected_result
