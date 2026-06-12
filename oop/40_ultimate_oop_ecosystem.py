"""
Task 40: Ultimate OOP Ecosystem.

This program integrates advanced Object-Oriented Programming principles to create
a robust e-commerce simulation. It demonstrates the synergy between modular
architectures and magic methods to manage complex transactional lifecycles.

Key Features:

- Protocol-Oriented Design: Implements custom validation wrappers and descriptor-like
  logic to ensure strict type integrity across heterogeneous item classes.
- Magic Method Orchestration: Leverages operator overloading (**add**, **radd**)
  for seamless mathematical operations and context managers (**enter**, **exit**)
  to handle secure financial transaction states.
- Resource Lifecycle Management: Utilizes **call** for fluent interface interaction
  and **slots** in specialized classes to optimize memory footprint during
  high-frequency courier updates.
- Decoupled State Handling: Employs 'dataclass' meta-programming for transparent
  data management, ensuring that logging, order tracking, and payment processing
  remain modular and decoupled within the broader system ecosystem.
"""

from dataclasses import dataclass, InitVar, field
from datetime import datetime


class LowBalanceError(Exception):
    pass


def check_str(data: str):
    if data is not None and not isinstance(data, str):
        raise TypeError("The data type must be a string")


def check_int(data: int):
    if data is not None and not isinstance(data, (int, float)):
        raise TypeError("The data type must be a int")


def check_cls(data):
    if not isinstance(data, (ItemCard, OnSale, ShoppingCart)):
        raise TypeError("The data type must be an instance of the class")


@dataclass
class SystemLogger:
    items: InitVar[list]
    total: InitVar[int]
    orders: list = field(default_factory=list)

    def __post_init__(self, items, total):
        self.orders.append({"items": items, "price": total})


class ItemCard:
    def __init__(self, category: str, title: str, price: int) -> None:
        check_str(category)
        check_str(title)
        check_int(price)

        self.category = category
        self._title = title
        self._price = price

    @property
    def price(self) -> str:
        return f"The item {self._title} costs {self._price}"

    @price.setter
    def price(self, value: int | float) -> None:
        check_int(value)

        if value > 0:
            self._price = value

    def __repr__(self) -> str:
        return f"[{self.category}] {self._title} - Price ({self._price})"

    def __add__(self, other):
        val = other.get_price() if isinstance(other, ItemCard) else other
        return self.get_price() + val

    def __radd__(self, other):
        return self.__add__(other)

    def get_price(self) -> int | float:
        return self._price


class OnSale(ItemCard):
    def __init__(self, category: str, title: str, price: int, discount: int) -> None:
        super().__init__(category, title, price)

        check_int(discount)
        self._discount = discount

    def get_price(self) -> int | float:
        return self._price * (100 - self._discount) / 100


class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.count = 0

    def __call__(self, item: ItemCard | OnSale):
        check_cls(item)
        self.cart.append(item)

    def __len__(self):
        return len(self.cart)

    def __bool__(self):
        return bool(self.cart)

    def __iter__(self):
        for item in self.cart:
            yield item

    def total_amount(self):
        return sum(item.get_price() for item in self.cart)


class SecurePayment:
    def __init__(self, cart: ShoppingCart, balance: int):
        check_cls(cart)
        check_int(balance)
        self.cart = cart
        self.balance = balance

    def __enter__(self):
        items = list(self.cart)
        total = self.cart.total_amount()

        if total > self.balance:
            print(
                "The transaction has been canceled, and the items have been returned to the warehouse"
            )
            raise LowBalanceError

        self.balance -= total
        return SystemLogger(items, total)

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            raise


class Courier:
    __slots__ = ["name", "transport", "status"]

    def __init__(self, name: str, transport: str, status: str):
        check_str(name)
        check_str(transport)
        check_str(status)
        self.name = name
        self.transport = transport
        self.status = status


@dataclass
class Order:
    data: datetime = field(default_factory=datetime.now)


if __name__ == "__main__":
    dress = ItemCard("Clothing", "Dress", 400)
    print(dress)  # [Clothing] Dress - Price (400)

    wristwatch = ItemCard("Watches", "Wristwatch", 700)
    print(dress + wristwatch)  # 1100
    print(700 + dress)  # 1100

    docker_cap = OnSale("Cap", "Dockerc cap", 200, 50)
    print(docker_cap.price)  # The item Dockerc cap costs 100.0

    ruslan_cart = ShoppingCart()
    ruslan_cart(docker_cap)
    ruslan_cart(wristwatch)

    print(
        ruslan_cart.cart
    )  # [[Cap] Dockerc cap - Price (200), [Cap] Dockerc cap - Price (200)]
    print(len(ruslan_cart))  # 2
    if not ruslan_cart:
        print("The cart is empty")
    else:
        print("The carst isn't empty")  # The carst isn't empty

    for item in ruslan_cart:
        print(
            item
        )  # -> [Cap] Dockerc cap - Price (200) -> [Watches] Wristwatch - Price (700)

    with SecurePayment(ruslan_cart, 9000) as payment:
        print(payment)

    courier = Courier("Alex", "Bicycle", "In transit")
