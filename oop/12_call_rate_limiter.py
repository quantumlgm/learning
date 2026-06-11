"""
Design a class-based decorator named `RateLimiter` using the `__call__` 
magic method to restrict how frequently a decorated function can be executed.

Requirements:
1. Initialization (`__init__`):
   - Accepts the target function `func` and stores it.
   - Initializes a tracking attribute `last_called` to 0 to keep track of 
     the timestamp of the last successful execution (use `time.time()`).

2. Execution Control (`__call__`):
   - Enforces a strict cooldown period of 2.0 seconds between successful 
     function calls.
   - When the decorated function is invoked:
     * If the elapsed time since `last_called` is LESS than 2.0 seconds, block 
     the execution, print "Too fast! Request blocked.", and return None.
     * If the elapsed time is GREATER than or EQUAL to 2.0 seconds, update `last_called` 
     to the current timestamp, execute the original function with `*args` and `**kwargs`, and return its result.
"""


import time
from typing import Callable

class RateLimiter:
    def __init__(self, func: Callable) -> None:
        self.last_called = 0
        self._func = func

    def __call__(self, *args, **kwds) -> None:        
        current_time = time.time()

        if current_time - self.last_called < 2:
            print("Too fast! Request blocked")
            return None
        else:
            self.last_called = current_time
            return self._func(*args, **kwds)                        

if __name__ == '__main__':

    @RateLimiter
    def query(name: str) -> str:
        return f"Hello, {name}!"
        
    print(query("Ruslan"))  # Hello, Ruslan!
        
    print(query("Max"))   # Too fast! Request blocked. -> None
        
    time.sleep(2.1)
        
    print(query("Quantum"))  # Выведет: Hello, John!
    