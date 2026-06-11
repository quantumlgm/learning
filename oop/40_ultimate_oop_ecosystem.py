


class SystemLogger:
    orders = {}
    def __init__(self):
        self.__dict__ = self.orders

class ItemCard:
    def __init__(self, category: str, title: str, price: int) -> None:
        self.category = category
        self._title = title
        self._price = price

    @property
    def price(self) -> str:
        return f"The item {self.title} costs {self.price}"
    
    @price.setter
    def price(self, value: int | float) -> None:
        if value > 0:
            self.price = value

    def __repr__(self) -> str:
        return f'[{self.category}] {self._title } - Price ({self._price})'
    
    def __add__(self, other):
        return self._price + other
    
    def __radd__(self, other):
        return self.__add__(other)
    
class OnSale(ItemCard):
    def __init__(self, category, title, price, discount):
        super().__init__(category, title, price)
        self._discount = discount

    @property
    def price(self) -> str:
        return f"The item {self._title} costs {self._price * (100 - self._discount) / 100}"    
    

if __name__ == "__main__":
    dress = ItemCard('Clothing', 'Dress', 400)
    print(dress) # [Clothing] Dress - Price (400)

    wristwatch = ItemCard('Watches', 'Wristwatch', 700)
    print(dress + wristwatch) # 1100    
    print(700 + dress) # 1100

    docker_cap = OnSale("Cap", "Dockerc cap", 200, 50)
    print(docker_cap.price) # The item Dockerc cap costs 100.0



