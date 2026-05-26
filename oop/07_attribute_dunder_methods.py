# Design a class named `SmartSafe` that intercepts all attribute operations (getting, 
# setting, deleting, and handling missing attributes) using Python's dunder methods.

# Requirements:
# 1. Instance Initialization (`__init__`):
#    - Accepts `code` (str) and `gold` (int/float).

# 2. Attribute Interception Logs:
#    - `__getattribute__(self, item)`: Intercepts EVERY read attempt. Prints `[ACCESS] Attempt to read attribute: <item>` and returns the actual value.
#    - `__setattr__(self, key, value)`: Intercepts EVERY write attempt. Prints `[CHANGE] Setting attribute <key> to <value>` and saves the value.
#    - `__getattr__(self, item)`: Intercepts missing attributes ONLY. Prints `[WARNING] Attribute <item> does not exist!` and returns `0`.
#    - `__delattr__(self, item)`: Intercepts deletion attempts. Prints `[SECURITY] Denied! Cannot delete <item>` and PREVENTS the deletion.

# CRITICAL CAUTION (Self-Study Warning):
# Be extremely careful with recursion! Remember how `__setattr__` and `__getattribute__` can 
# accidentally call themselves indefinitely if you use standard dot notation inside them. Use `super()` to bypass the infinite loops.


class SmartSafe:
    def __init__(self, code: str, gold: int | float) -> None:
        self.code = code
        self.gold = gold

    def __getattribute__(self, name: str) -> None:
        print(f'[ACCESS] Attempt to read attribute: {name}')
        return object.__getattribute__(self, name)

    def __setattr__(self, name: str, value) -> None:
        print(f'[CHANGE] Setting attribute {name} to {value}')
        return object.__setattr__(self, name, value)
    
    def __getattr__(self, name: str) -> int:
        print(f'[WARNING] Attribute {name} does not exist!')               

    def __delattr__(self, name: str) -> None:
        print(f'[SECURITY] Denied! Cannot delete {name}')        


if __name__ == "__main__":
    Safe = SmartSafe('Quantumlgm', 5000) # [CHANGE] Setting attribute code to Quantumlgm
                                         # [CHANGE] Setting attribute gold to 5000
    Safe.gold # [ACCESS] Attempt to read attribute: gold
    Safe.diamond # [WARNING] Attribute diamond does not exist!
    del Safe.gold # [SECURITY] Denied! Cannot delete gold
    print(Safe.__dict__) # [ACCESS] Attempt to read attribute: __dict__
                         # {'code': 'Quantumlgm', 'gold': 5000}
    
