# Create a robust `SafeDivider` class that processes string inputs, 
# converts them to floats, and performs division while safely handling 
# potential exceptions.

# Requirements:
# 1. Class `SafeDivider`:
#    - Implement a method `divide(val1: str, val2: str) -> float | str`.
#    - Wrap the conversion and division logic inside a try-except structure.
#    - Catch `ValueError` specifically if inputs cannot be parsed into floats.
#    - Catch `ZeroDivisionError` specifically if the denominator evaluates to zero.
#    - Catch any other generic `Exception` as a fallback.
#    - Return appropriate error messages as specified in the instructions 
#      rather than letting the application crash.