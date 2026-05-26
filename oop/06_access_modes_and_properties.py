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


from accessify import private

class DigitalWallet:
    def __init__(self, owner: str, balance: int) -> None:
        self._owner = owner
        self.__balance = balance

    def get_balance(self) -> int | float:
        return self.__balance
    
    @private
    def set_balance(self, amnout: int | float) -> str:
        if isinstance(amnout, (int, float)) and amnout >= 0:
            self.__balance += amnout
            return 'The balance has been updated'        
        return 'You cannot top up your balance by this amount'
    
    def deposit(self, amnout: int | float):
        print(self.set_balance(amnout))

    



if __name__ == "__main__":
    Wallet = DigitalWallet('Ruslan', 1000)
    print(Wallet.__dict__) # {'_owner': 'Ruslan', '_DigitalWallet__balance': 1000}

    # Wallet.set_balance(1000) -> InaccessibleDueToItsProtectionLevelException

    Wallet.deposit(1000) # The balance has been updated
    print(Wallet.__dict__) # {'_owner': 'Ruslan', '_DigitalWallet__balance': 2000}


