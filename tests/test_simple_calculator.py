"""
Title : test_simple_calculator.py

Objective : This module contains unit tests for the SimpleCalculator class defined in simple_calculator.py.
It tests the basic arithmetic operations: addition, subtraction, multiplication, and division,
including edge cases such as division by zero.

Author : Yanis PIRES PORTELADA

Date : 2026-02-12
"""

from calculator import SimpleCalculator


calc = SimpleCalculator()

def test_add():
    res = calc.add(2, 3)
    return res

def test_substract():
    res = calc.substract(2, 3)
    return res

def test_multiply():
    res = calc.multiply('nah', 3)
    return res

def test_divide():
    res = calc.divide(0,4)
    return res
    
# print(test_add())
# print(test_substract())
# print(test_multiply())
print(test_divide())
