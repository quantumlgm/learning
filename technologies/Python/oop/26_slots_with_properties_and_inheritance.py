"""
Design an optimized class hierarchy for spaceship telemetry
using `__slots__` combined with `@property` descriptors to
enforce memory layout and data validation during inheritance.

Requirements:
1. Base Class `EngineTelemetry`:
   - Define `__slots__` to hold strictly `_speed` and `_fuel`.
   - Implement an initializer to set these internal slotted attributes.
   - Implement `@property` pairs (getter/setter) for `speed` and `fuel`.
   - The `fuel` setter must validate inputs: if a negative value is
     passed, clip it to 0.

2. Subclass `FullTelemetry`:
   - Inherit from `EngineTelemetry`.
   - Define `__slots__` explicitly to contain only the new attribute
     `_oxygen`. This ensures `__dict__` remains disabled for the subclass.
   - Implement an initializer that leverages `super()` and sets `_oxygen`.
   - Implement a read-only `@property` (getter only) for `oxygen`.
"""


class EngineTelemetry:
    __slots__ = ("_speed", "_fuel")

    def __init__(self, speed: int, fuel: int) -> None:
        self._speed = speed
        self._fuel = fuel

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed: int) -> None:
        self._speed = speed

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel: int) -> None:
        self._fuel = max(0, fuel)


class FullTelemetry(EngineTelemetry):
    __slots__ = ("_oxygen",)

    def __init__(self, speed: int, fuel: int, oxygen: int) -> None:
        super().__init__(speed, fuel)
        self._oxygen = oxygen

    @property
    def oxygen(self) -> int:
        return self._oxygen


if __name__ == "__main__":
    engine = EngineTelemetry(150, 1000)
    print(engine.__slots__)  # ('_speed', '_fuel')

    ship = FullTelemetry(200, 1500, 100)
    print(ship.__slots__)  # ('_oxygen',)
    print(f"fuel: {ship.fuel}, speed: {ship.speed}")
    ship.fuel = -10
    print(ship.fuel)  # 0
    try:
        ship.crew = ("Quantum", "Ruslan", "Linus Torvalds")
    except AttributeError:
        print(
            "AttributeError: 'FullTelemetry' object has no attribute 'crew'"
        )  # AttributeError: 'FullTelemetry' object has no attribute 'crew'
