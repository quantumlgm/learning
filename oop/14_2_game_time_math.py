# Design a class named `GameTime` to manage and track player session durations in minutes,
# utilizing comprehensive arithmetic operator overloading (+, -, *, and their in-place equivalents).

# Requirements:
# 1. Initialization & Representation:
#    - Accepts `minutes` (int) and stores it internally.
#    - Implement `__str__` to output a human-readable format like: "X hr Y min".

# 2. Operator Overloading:
#    - Implement `__add__` / `__radd__` / `__iadd__`: Support adding numeric values
#      (minutes) or other `GameTime` instances, ensuring proper in-place object
#       mutation for `+=`.
#    - Implement `__sub__` / `__rsub__` / `__isub__`: Support subtracting numeric
#      values or other instances. Pay special attention to right-side subtraction (`__rsub__`) where order of operands matters.
#    - Implement `__mul__` / `__rmul__` / `__imul__`: Support multiplying the game session length by a numeric scaling factor.


from __future__ import annotations
from typing import Self


class GameTime:
    def __init__(self, minutes: int) -> None:
        self._minutes = minutes

    def __str__(self):
        return f"{self._minutes // 60} hr {self._minutes % 60} min"

    def __add__(self, other: int | float | GameTime) -> GameTime:
        if isinstance(other, (int, float)):
            return GameTime(self._minutes + other)
        if isinstance(other, GameTime):
            return GameTime(self._minutes + other._minutes)
        return NotImplemented

    def __radd__(self, other) -> GameTime:
        if isinstance(other, (int, float)):
            return self.__add__(other)
        return NotImplemented

    def __iadd__(self, other) -> Self:
        if isinstance(other, (int, float)):
            self._minutes += other
            return self

    def __sub__(self, other) -> GameTime:
        if isinstance(other, (int, float)):
            return GameTime(self._minutes - other)
        if isinstance(other, GameTime):
            return GameTime(self._minutes - other._minutes)
        return NotImplemented

    def __rsub__(self, other) -> GameTime:
        if isinstance(other, (int, float)):
            return GameTime(other - self._minutes)
        return NotImplemented

    def __isub__(self, other) -> Self:
        if isinstance(other, (int, float)):
            self._minutes -= other
            return self

    def __mul__(self, other) -> GameTime:
        if isinstance(other, (int, float)):
            return GameTime(self._minutes * other)
        return NotImplemented

    def __rmul__(self, other) -> GameTime:
        if isinstance(other, (int, float)):
            return self.__mul__(other)
        return NotImplemented

    def __imul__(self, other) -> Self:
        if isinstance(other, (int, float)):
            self._minutes *= other
            return self


if __name__ == "__main__":
    t1 = GameTime(80)
    t2 = GameTime(50)
    print(t1)  # 1 hr 20 min
    print(t1 + t2)  # 2 hr 10 min
    print(t1 + 10)  # 1 hr 30 min
    print(10 + t1)  # 1 hr 30 min
    print(t1 - t2)  # 0 hr 30 min
    print(120 - t1)  # 0 hr 40 min
    print(t1 * 2)  # 2 hr 40 min
    print(2 * t1)  # 2 hr 40 min
    t1 += 20
    t2 -= 10
    print(t1)  # 1 hr 40 min
    print(t2)  # 0 hr 40 min
