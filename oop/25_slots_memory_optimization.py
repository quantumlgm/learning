"""
Design an optimized base class `MassUnit` using `__slots__` and a
flexible subclass `HeroUnit` to demonstrate how Python handles memory
optimization and attribute restrictions.

Requirements:
1. Class `MassUnit`:
   - Use `__slots__` to restrict attributes strictly to 'x', 'y', and 'hp'.
   - Implement an initializer to set these three attributes.
   - Implement a `move(dx, dy)` method to update coordinates in-place.

2. Subclass `HeroUnit`:
   - Inherit from `MassUnit`.
   - Do NOT define `__slots__` in this subclass, allowing Python to automatically
     re-enable `__dict__` for dynamic attributes.
   - Implement an initializer that sets base attributes via the parent
     class and adds a custom 'name' attribute.
"""


class MassUnit:
    __slots__ = ("x", "y", "hp")

    def __init__(self, x: int, y: int, hp: int) -> None:
        self.x = x
        self.y = y
        self.hp = hp

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy


class HeroUnit(MassUnit):
    def __init__(self, x: int, y: int, hp: int, name: str) -> None:
        super().__init__(x, y, hp)
        self.name = name


if __name__ == "__main__":
    mass_unit = MassUnit(25, 45, 90)
    print(mass_unit.__slots__)  # ('x', 'y', 'hp')
    try:
        print(mass_unit.__dict__)  # AttributeError:...
    except AttributeError:
        print("AttributeError. No dict for mass unit")

    hero_unit = HeroUnit(10, 15, 100, "wizard")
    print(hero_unit.__slots__)  # ('x', 'y', 'hp')
    print(hero_unit.__dict__)  # {'name': 'wizard'}

    hero_unit.move(55, 55)
    print(f"x: {hero_unit.x}, y: {hero_unit.y}")  # x: 65, y: 70
    hero_unit.move(-10, 0)
    print(f"x: {hero_unit.x}, y: {hero_unit.y}")  # x: 55, y: 70
    hero_unit.weapon = "Knife"
    print(hero_unit.weapon)  # Knife
