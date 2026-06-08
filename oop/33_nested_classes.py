"""
Implement a bank account management system utilizing nested classes to separate account holder data from tariff configuration rules (encapsulation and data isolation).

Requirements:
1. Static Helper Validation:
   - Implement standalone functions `check_str` and `check_int` to validate data types and raise standard `TypeError` on failure.

2. Nested Class `Tariff`:
   - Define a nested class `Tariff` inside `Account` to store tariff rules.
   - It must encapsulate `plan_name` (str) and `commission` (float/int rate).

3. Main Class `Account`:
   - Initialize `owner`, `balance`, and instantiate the nested `Tariff` object during setup.
   - Implement `refill(amount)` to increase the current balance.
   - Implement `withdrawal(amount)` to decrease the balance by the requested amount plus the corresponding tariff commission fee.
   - Implement `info()` to return a formatted summary string containing the owner's name, balance, and tariff plan name.
"""

def check_str(data: str):
    if not isinstance(data, str):
        raise TypeError("The data type must be a string")


def check_int(data: int):
    if not isinstance(data, (int, float)):
        raise TypeError("The data type must be a int")


class Account:
    def __init__(self, owner: str, balance: int, plan: str, commission: int) -> None:
        check_str(owner)
        check_int(balance)
        check_str(plan)
        check_int(commission)

        self.owner = owner
        self.balance = balance
        self.tariff = self.Tariff(plan, commission)

    def refill(self, amount: int) -> None:
        check_int(amount)
        self.balance += amount

    def withdrawal(self, amount: int):
        check_int(amount)
        total = amount + (amount * self.tariff.commission)
        self.balance -= total

    def info(self) -> str:
        return f"[INFO] balance: {self.balance}, owner: {self.owner}, plan: {self.tariff.plan_name}"

    class Tariff:
        def __init__(self, plan_name, commission):
            self.plan_name = plan_name
            self.commission = commission


if __name__ == "__main__":
    Ruslan = Account("Ruslan", 10000, "Standard", 0.05)
    print(Ruslan.info())  # [INFO] balance: 10000, owner: Ruslan, plan: Standard

    Quantum = Account("Quantum", 50000, "Premium", 0.01)
    print(Quantum.info())  # [INFO] balance: 50000, owner: Quantum, plan: Premium

    Ruslan.withdrawal(1000)
    print(Ruslan.info())  # [INFO] balance: 8950.0, owner: Ruslan, plan: Standard

    Ruslan.refill(500)
    print(Ruslan.info())  # [INFO] balance: 9450.0, owner: Ruslan, plan: Standard
