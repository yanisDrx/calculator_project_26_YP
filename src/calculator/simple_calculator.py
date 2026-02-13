"""
Title: simple_calculator.py

Objective: A simple calculator module that provides basic arithmetic operations:
addition, subtraction, multiplication, and division.

Author: Yanis PIRES PORTELADA

Date: 2026-02-12
"""

class SimpleCalculator:
    """
    A simple calculator that provides basic arithmetic operations
    on integer operands.
    """
    def __init__(self):
        pass

    def _validate_operands(self, a: object, b: object) -> None:
        """Validates that both operands are integers and not None."""
        if not isinstance(a, int) or not isinstance(b, int) or a is None or b is None:
            raise ValueError("Error: Both operands must be integers")

    def add(self, a: int, b: int) -> int:
        """Returns the sum of a and b."""
        self._validate_operands(a, b)
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Returns the difference of a and b."""
        self._validate_operands(a, b)
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Returns the product of a and b."""
        self._validate_operands(a, b)
        return a * b

    def divide(self, a: int, b: int) -> float:
        """Returns the quotient of a and b. Raises an error if b is zero."""
        self._validate_operands(a, b)
        if b != 0:
            return a / b
        raise ValueError("Error: Division by zero")
