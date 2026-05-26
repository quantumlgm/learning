# Design a class named `DigitalWallet` that demonstrates encapsulation using protected (_) and 
# private (__) access modifiers, along with explicit getter and setter methods.

# Requirements:
# 1. Instance Initialization (`__init__`):
#    - Accepts `owner` (str) and `initial_balance` (int/float).
#    - Store the owner's name as a protected attribute: `_owner`.
#    - Store the balance as a private attribute: `__balance`. Initialize it using the validation 
#      logic from your setter.

# 2. Access and Validation Methods (Getters / Setters):
#    - `get_balance(self) -> int/float`: Returns the current value of the private balance.
#    - `set_balance(self, amount: int/float) -> None`: Validates the input. If `amount` is a 
#       number (int or float) and is greater than or equal to 0, update the private balance. 
#       Otherwise, reject the modification.

# 3. Business Logic:
#    - `deposit(self, amount: int/float) -> None`: Safely increments the wallet's balance 
#       by the given `amount` using the internal `set_balance` logic.


