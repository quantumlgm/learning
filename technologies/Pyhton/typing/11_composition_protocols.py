"""
Lesson 11: Protocol Composition and Generic Constraints

Short Description:
A practical implementation of Interface Segregation Principle (ISP)
using generic protocol inheritance and structural type validation.

Detailed Description:
This module demonstrates how to assemble fine-grained interfaces into complex contracts:
- Combines standalone generic protocols 'HelpForRead[T]' and 'HelpForWrite[T]'
  into a unified 'HelpForReadWrite[T]' composite protocol.
- Validates structural invariance where 'ParseString' satisfies 'HelpForReadWrite[str]',
  while 'ParseInt' is correctly caught by Pyright due to generic type mismatch.
"""

from typing import Protocol


class HelpForRead[T](Protocol):
    def read(self, data: T) -> T: ...


class HelpForWrite[T](Protocol):
    def write(self, data: T) -> None: ...


class HelpForReadWrite[T](HelpForRead[T], HelpForWrite[T], Protocol): ...


def parse(data: HelpForReadWrite[str], source: str) -> None:
    print(data.read(source))
    data.write(source)


class ParseString:
    def __init__(self):
        self.storage: list[str] = []

    def read(self, data: str) -> str:
        return data

    def write(self, data: str) -> None:
        self.storage.append(data)


class ParseInt:
    def __init__(self):
        self.storage: list[int] = []

    def read(self, data: int) -> int:
        return data

    def write(self, data: int) -> None:
        self.storage.append(data)


if __name__ == "__main__":
    string = ParseString()
    print(string.read("It's a string"))

    string.write("I've wrote a string")
    print(string.storage)  # ["I've wrote a string"]

    parse(string, "String")  # String
