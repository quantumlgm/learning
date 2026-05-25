# Design a class named `WeavingLoom` that simulates an industrial weaving machine. This task focuses heavily on understanding how `self` 
# binds an instance to class methods and how methods can be invoked explicitly.

# Requirements:
# 1. Class Attributes:
#    - `default_color` (str): Set to "white".
#    - `max_speed` (int): Set to 100.

# 2. Instance Initialization (`__init__`):
#    - Accepts an optional `speed` (int) parameter. If not provided or if it exceeds `max_speed`, fallback to the class `max_speed`.
#    - Do NOT define a color attribute inside `__init__`. The instance's __dict__ must remain clear of any color keys upon creation.

# 3. Methods to implement:
#    - `get_current_color(self) -> str`: Returns the custom color of the instance if it has one. If the instance doesn't 
#       have a specific color, it must look up and return the class `default_color`.
#    - `fabricate(self) -> None`: Prints a status message stating the current operation, using the loom's actual speed 
#       and the color retrieved by `get_current_color`.
#    - `set_exclusive_color(self, new_color: str) -> None`: This method is used to set a unique color directly onto the instance's dictionary.

# 4. Execution Restrictions (The 'Self' Mastery Test):
#    - In your execution block (`if __name__ == "__main__":`), you must create an instance of `WeavingLoom`.
#    - You must call the `set_exclusive_color` method EXPLICITLY through the Class, passing the instance manually 
#      as the first argument (simulating what Python does under the hood). Do not use the `instance.method()` syntax for this specific action.

class WeavingLoom:
    default_color = "white"
    max_speed = 100

    def __init__(self, speed=None) -> None:
        if speed is None or speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed = abs(speed)
        
    def get_current_color(self) -> str:
        return getattr(self, "color", self.default_color)
    
    def fabricate(self) -> None:
        return {'current_speed': self.speed, "current_color": self.get_current_color()}
    
    def set_exclusive_color(self, new_color: str) -> None:
        self.color = new_color
        return self.color

            

if __name__ == '__main__':
    Loom = WeavingLoom(100)
    print(Loom.__dict__) # {'speed': 100}

    print(Loom.get_current_color()) # white
    print(Loom.__dict__)

    print(Loom.fabricate()) # {'current_speed': 100, 'current_color': 'white'}
    print(Loom.__dict__)

    print(Loom.set_exclusive_color('blue')) # blue
    print(Loom.__dict__)

    print(WeavingLoom.set_exclusive_color(Loom, 'red')) # red
    print(Loom.__dict__)
