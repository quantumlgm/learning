# Design a class named `SmartWatch` that enables full comparison capabilities (==, !=, <, <=, >, >=) 
# between different watch instances or between a watch instance and a numeric price using magic methods.

# Requirements:
# 1. Initialization:
#    - Accepts `model` (str) and `price` (int).

# 2. Comparison Methods:
#    - Implement `__eq__`: Compare the `price` of the current watch with another 
#      `SmartWatch` instance or a numeric value (int/float). Return NotImplemented 
#       for unsupported types.
#    - Implement `__lt__`: Check if the current watch `price` is strictly less than 
#      the other watch's price or a numeric value.
#    - Implement `__le__`: Check if the current watch `price` is less than or 
#      equal to the other watch's price or a numeric value.


class SmartWatch:
    def __init__(self, model: str, price: int) -> None:
        self.model = model
        self.price = price

    def __eq__(self, other):
        if isinstance(other, SmartWatch):
            return self.price == other.price
        if isinstance(other, int):
            return self.price == other
    
    def __lt__(self, other):
        if isinstance(other, SmartWatch):
            return self.price < other.price
        if isinstance(other, int):
            return self.price < other
        
    def __le__(self, other):
        if isinstance(other, SmartWatch):
            return self.price <= other.price
        if isinstance(other, int):
            return self.price <= other
        
if __name__ == '__main__':
    w1 = SmartWatch("Apple Watch ", 400)
    w2 = SmartWatch("Samsung Galaxy Watch", 300)
    w3 = SmartWatch("Xiaomi Watch", 400) 

    print(w1 == w2) # False 
    print(w1 == w3) # True 
    print(w1 != w2) # True 
    print(w1 <= w3) # True
    print(w2 <= w3) # True
    print(w1 >= 400)