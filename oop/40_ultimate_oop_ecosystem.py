


def check_str(data: str):
    if data is not None and not isinstance(data, str):
        raise TypeError("The data type must be a string")


def check_int(data: int):
    if data is not None and not isinstance(data, (int, float)):
        raise TypeError("The data type must be a int")


class SystemLogger:
    orders = {}
    def __init__(self):
        self.__dict__ = self.orders

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
        return f"The item {self.title} costs {self.price}"
    
    @price.setter
    def price(self, value: int | float) -> None:        
        check_int(value)

        if value > 0:
            self.price = value

    def __repr__(self) -> str:
        return f'[{self.category}] {self._title } - Price ({self._price})'
    
    def __add__(self, other):                        
        return self._price + other
    
    def __radd__(self, other):        
        return self.__add__(other)
    
    
class OnSale(ItemCard):
    def __init__(self, category: str, title: str, price: int, discount: int) -> None:
        super().__init__(category, title, price)                
        
        check_int(discount)
        self._discount = discount

    @property
    def price(self) -> str:
        return f"The item {self._title} costs {self._price * (100 - self._discount) / 100}"    
    

class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.count = 0

    def __call__(self, item: ItemCard | OnSale):
        if not isinstance(item, (ItemCard, OnSale)):
            raise TypeError("The item must extend the ItemCard or OnSale class")
        self.cart.append(item)        
        
    def __len__(self):
        return len(self.cart)
    
    def __bool__(self):
        return bool(self.cart)
    
    def __iter__(self):
        for item in self.cart:
            yield item


class SecurePayment
        
            
if __name__ == "__main__":
    dress = ItemCard('Clothing', 'Dress', 400)
    print(dress) # [Clothing] Dress - Price (400)

    wristwatch = ItemCard('Watches', 'Wristwatch', 700)
    print(dress + wristwatch) # 1100    
    print(700 + dress) # 1100

    docker_cap = OnSale("Cap", "Dockerc cap", 200, 50)
    print(docker_cap.price) # The item Dockerc cap costs 100.0

    ruslan_cart = ShoppingCart()
    ruslan_cart(docker_cap) 
    ruslan_cart(wristwatch) 

    print(ruslan_cart.cart) # [[Cap] Dockerc cap - Price (200), [Cap] Dockerc cap - Price (200)]
    print(len(ruslan_cart)) # 2
    if not ruslan_cart:
        print('The cart is empty')
    else:
        print("The carst isn't empty") # The carst isn't empty

    for item in ruslan_cart:
        print(item) # -> [Cap] Dockerc cap - Price (200) -> [Watches] Wristwatch - Price (700)

