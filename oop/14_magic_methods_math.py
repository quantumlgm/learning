"""
Design a class named `ShoppingCart` that manages the total cost of items and
supports addition operations (+ and +=) using magic methods.

Requirements:
1. Initialization:
   - Accepts an optional `total_price` (int/float, defaults to 0).

2. Magic Methods:
   - Implement `__add__`: If `other` is a number (int/float) or another
     `ShoppingCart` instance, return a NEW `ShoppingCart` object with the combined total price.
   - Implement `__radd__`: Enable right-side addition (e.g., `100 + cart`)
      by reusing the `__add__` logic.
   - Implement `__iadd__`: Modify the CURRENT instance's `total_price` in-place
     when using `+=` with a number. Ensure it returns `self`.
"""


class ShoppingCart:
    def __init__(self, totatl_price):
        self.total_price = totatl_price

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return ShoppingCart(self.total_price + other)
        else:
            return ShoppingCart(self.total_price + other.total_price)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.total_price += other
            return self


if __name__ == "__main__":
    cart1 = ShoppingCart(100)
    cart2 = ShoppingCart(200)

    cart3 = cart1 + cart2
    print(cart3.total_price)  # 300

    cart4 = cart1 + 50
    print(cart4.total_price)  # 150

    cart5 = 50 + cart1
    print(cart5.total_price)  # 150

    cart1 += 500
    print(cart1.total_price)  # 600
