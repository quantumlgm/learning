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


class GlobalLogger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
        
    def __init__(self, log_level: str) -> None:
        if hasattr(self, 'log_level'):
            return
        self.log_level = log_level

    def log(self, message: str) -> str:
        return f"[{self.log_level}] {message}"
    

if __name__ == "__main__":
    print(GlobalLogger.__dict__) # '_GlobalLogger__instance': None
    Logger = GlobalLogger('INFO') 
    print(Logger.__dict__)# {'log_level': 'INFO'}
    print(GlobalLogger.__dict__) # _GlobalLogger__instance': <__main__.GlobalLogger object at 0x0000022995C56CF0>
    Logger = GlobalLogger('DEBUG') 
    print(Logger.__dict__) # {'log_level': 'INFO'}
    print(GlobalLogger.__dict__) # _GlobalLogger__instance': <__main__.GlobalLogger object at 0x0000022995C56CF0>
