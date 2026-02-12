

class Calculator:
    
    def __init__(self):
        pass
    
    def add(self, a: int, b: int) -> int:
        """Returns the sum of a and b."""
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Returns the difference of a and b."""
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Returns the product of a and b."""
        return a * b

    def divide(self, a: int, b: int):
        """Returns the quotient of a and b. If b is zero, returns an error message."""
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
        









# from math import sqrt

# def calculator(a : int, b : int, operation : str):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         return a - b
#     elif operation == "multiply":
#         return a * b
#     elif operation == "divide":
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Error: Invalid operation"
    
    
# print(calculator(10, 5, "add"))