
def check_str(data: str):
    for d in data:
        if not isinstance(d, str):
            raise TypeError("The data type must be a string")

def check_int(data: int):
    if not isinstance(data, int):
        raise TypeError("The data type must be a int")


class Account:
    def __init__(self, owner: str, balance: int, plan: str, commission: int) -> None:
        check_str((owner, plan))
        check_int(balance)
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


if __name__ == '__main__':
    Ruslan = Account("Ruslan", 10000, 'Standard', 0.05)
    print(Ruslan.info()) # [INFO] balance: 10000, owner: Ruslan, plan: Standard

    Quantum = Account('Quantum', 50000, 'Premium', 0.01)
    print(Quantum.info()) # [INFO] balance: 50000, owner: Quantum, plan: Premium

    Ruslan.withdrawal(1000)
    print(Ruslan.info()) # [INFO] balance: 7999.95, owner: Ruslan, plan: Standard