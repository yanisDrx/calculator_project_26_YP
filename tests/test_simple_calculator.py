"""
Title : test_simple_calculator_manual.py

Objective : Simple unit tests for the SimpleCalculator class
without using pytest. Uses assert and try/except to check behavior.

Author : Yanis PIRES PORTELADA

Date : 2026-02-12
"""

from calculator import SimpleCalculator

calc = SimpleCalculator()

# Test for add()
def test_add():
    """Tests the add() method for valid and invalid inputs."""
    # valid tests
    assert calc.add(2, 3) == 5
    assert calc.add(0, 0) == 0
    assert calc.add(-2, 3) == 1

    # invalid tests
    for a, b in [('nah', 3), (0.4, 3), (None, 2)]:
        try:
            calc.add(a, b)
            print(f"ERROR: add({a}, {b}) did not raise ValueError")
        except ValueError:
            print(f"PASS: add({a}, {b}) raised ValueError")


# Test for subtract()
def test_subtract():
    """Tests the subtract() method for valid and invalid inputs."""
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(-2, -3) == 1

    for a, b in [('nah', 3), (0.4, 3), (None, 2)]:
        try:
            calc.subtract(a, b)
            print(f"ERROR: subtract({a}, {b}) did not raise ValueError")
        except ValueError:
            print(f"PASS: subtract({a}, {b}) raised ValueError")


# Test for multiply()
def test_multiply():
    """Tests the multiply() method for valid and invalid inputs."""
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0
    assert calc.multiply(-2, 3) == -6

    for a, b in [('nah', 3), (0.4, 3), (None, 2)]:
        try:
            calc.multiply(a, b)
            print(f"ERROR: multiply({a}, {b}) did not raise ValueError")
        except ValueError:
            print(f"PASS: multiply({a}, {b}) raised ValueError")


# Test for divide()
def test_divide():
    """Tests the divide() method for valid inputs, zero division,
    and invalid inputs."""
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(-6, 3) == -2.0
    assert calc.divide(0, 5) == 0.0

    # dividing by zero should raise ValueError
    try:
        calc.divide(5, 0)
        print("ERROR: divide(5, 0) did not raise ValueError")
    except ValueError:
        print("PASS: divide(5, 0) raised ValueError")

    for a, b in [('nah', 3), (0.4, 3), (None, 2)]:
        try:
            calc.divide(a, b)
            print(f"ERROR: divide({a}, {b}) did not raise ValueError")
        except ValueError:
            print(f"PASS: divide({a}, {b}) raised ValueError")


# Running tests
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests have been executed.")
