# Design a class-based data descriptor named `PositiveNumber` to automate
# non-negative numeric validation for product parameters.

# Requirements:
# 1. Descriptor Class `PositiveNumber`:
#    - Implement `__set_name__(self, owner, name)` to dynamically create a
#      protected attribute name (e.g., `_price`).
#    - Implement `__set__(self, instance, value)`: Validate that the value
#      is an int or float, and is greater than or equal to 0. Raise a ValueError
#      if validation fails. Otherwise, store it inside `instance.__dict__`.
#    - Implement `__get__(self, instance, owner)`: Return the value from `instance.__dict__`.
#      If called from the class level, return the descriptor instance itself.

# 2. Main Class `Product`:
#    - Define two class-level attributes using the descriptor: `price` and `quantity`.
#    - Initialization accepts `name` (str), `price` (int/float), and `quantity` (int/float).


from typing import Any


class PositiveNumber:
    def __set_name__(self, owner: type, name: str) -> None:
        self.name = "_" + name

    def __set__(self, instance: Any, value: int | float) -> None:
        if isinstance(value, (int, float)) and value >= 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError("Invalid data type or value less than zero")

    def __get__(self, instance: Any, owner: type) -> int | float:
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]


class Product:
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name: str, price: int | float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

if __name__ == '__main__':
    Phone = Product('Honor', 1000.5, 20)
    print(Phone.__dict__) # {'name': 'Honor', '_price': 1000.5, '_quantity': 20}
    print(Phone.price) # 1000.5
    print(Phone.quantity) # 20
    Phone.name = 'Honor 200'
    print(Phone.name) # Honor 200
    Phone.price = 2000
    print(Phone.price) # 2000
