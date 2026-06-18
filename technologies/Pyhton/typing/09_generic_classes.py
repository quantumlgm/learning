"""
Lesson 09: Generic Classes and Generic Mappings (Python 3.12+)

Short Description:
A showcase of user-defined generic containers, custom read-only mappings,
and generic dataclasses using contemporary PEP 695 syntax.

Detailed Description:
This module validates class-level generics in modern Python:
- Implements a generic 'Wrapper[T]' encapsulation layer that preserves concrete types.
- Establishes a structured 'Maping[T, Y]' collection inheriting from 'Mapping',
  demonstrating how type parameters are cleanly forwarded to abstract base classes.
- Utilizes a generic '@dataclass' structure to safely handle highly dynamic
  payloads without type degradation or relying on 'Any'.
"""

from dataclasses import dataclass
from collections.abc import Mapping


class Wrapper[T]:
    def __init__(self, item: T) -> None:
        self.item: T = item


class Maping[T, Y](Mapping[T, Y]):
    def __init__(self, key: T, value: Y):
        self._storage: dict[T, Y] = {key: value}

    def __getitem__(self, key: T) -> Y:
        return self._storage[key]

    def __len__(self) -> int:
        return len(list(self._storage.values()))

    def __iter__(self):
        return iter(())


@dataclass
class Data[T]:
    status: str
    id: int
    data: T


if __name__ == "__main__":
    wrapper = Wrapper("Ruslan")
    print(wrapper.__dict__)  # {'item': 'Ruslan'}

    maping = Maping("Key", "value")
    print(maping.__dict__)  # {'_storage': {'Key': 'value'}}
    print(len(maping))  # 1

    data = Data("loaded", 1, [1, "x", {"a": 1}])
    print(data)  # Data(status='loaded', id=1, data=[1, 'x', {'a': 1}])
