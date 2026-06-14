from typing import Callable

type number = int | float


class RegisterCustomer:
    def __init__(self, name: str, loyalty: int, balance: number) -> None:
        self.name = name
        self.loyalty = loyalty
        self.balance = balance


def loyalty_program(customer: RegisterCustomer, cost: number) -> number:
    discount = cost * customer.loyalty / 100
    return discount


def black_friday_sale(customer: RegisterCustomer, cost: number) -> number:
    if cost > 5000:
        return 1000
    return 0.0


def payment_processing(
    cost: number,
    customer: RegisterCustomer,
    promotion: Callable[[RegisterCustomer, number], number],
) -> number:
    discount_amount: number = promotion(customer, cost)
    if discount_amount >= cost:
        return 0.0
    total = cost - discount_amount
    return total


if __name__ == "__main__":
    ruslan = RegisterCustomer("Ruslan", 15, 5000)
    print(ruslan.__dict__)  # {'name': 'Ruslan', 'loyalty': 15, 'balance': 0}

    shoes = 6000

    ruslan_payment = payment_processing(shoes, ruslan, loyalty_program)
    print(ruslan_payment)  # 5100.0

    ruslan_payment = payment_processing(shoes, ruslan, black_friday_sale)
    print(ruslan_payment)  # 5000
