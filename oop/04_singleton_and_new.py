# Design a class named `GlobalLogger` that implements the Singleton pattern to ensure only one 
# instance of the logger exists across the entire application.

# Requirements:
# 1. Singleton Mechanism:
#    - Implement the pattern using the `__new__` method.
#    - Store the unique instance reference in a private class-level attribute named `__instance`.
#    - If an instance already exists, subsequent instantiation calls must return the existing instance.

# 2. Instance Initialization (`__init__`):
#    - Accepts a `log_level` parameter (e.g., "INFO", "DEBUG").
#    - Guard against re-initialization: If the object has already been initialized in a previous call,
#      `__init__` must gracefully exit without overwriting the original `log_level`.

# 3. Interface:
#    - `log(self, message: str) -> None`: Prints the message to the console in the following format: `[{log_level}] {message}`.