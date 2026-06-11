"""
Create a robust `SafeDivider` class that processes string inputs, 
converts them to floats, and performs division while safely handling 
potential exceptions.

Requirements:
1. Class `SafeDivider`:
   - Implement a method `divide(val1: str, val2: str) -> float | str`.
   - Wrap the conversion and division logic inside a try-except structure.
   - Catch `ValueError` specifically if inputs cannot be parsed into floats.
   - Catch `ZeroDivisionError` specifically if the denominator evaluates to zero.
   - Catch any other generic `Exception` as a fallback.
   - Return appropriate error messages as specified in the instructions 
     rather than letting the application crash.
"""


class SafeDivider:
    def divide(self, val1: int | float | str, val2: int | float | str) -> int | float | str:
        try:
            val1, val2 = float(val1), float(val2)
            return val1 / val2
        except ValueError:
            return "Error: Inputs must be numeric values"
        except ZeroDivisionError:
            return "Error: Division by zero is forbidden"
        except Exception as e:
            return f"Unexpected error: {e}"


if __name__ == '__main__':
    devider = SafeDivider()
    print(devider.divide(10, 5)) # 2.0
    print(devider.divide(10, "2")) # 5.0
    print(devider.divide(10, 0)) # Error: Division by zero is forbidden
    print(devider.divide(10, 'a')) # Error: Inputs must be numeric values
