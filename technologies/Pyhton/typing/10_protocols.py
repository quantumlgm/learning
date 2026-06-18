"""
Lesson 10: Protocols vs Abstract Base Classes (ABC) & SOLID Principles

Short Description:
A comparative study of nominal typing via ABCs versus structural typing
via Protocols to achieve loose coupling and satisfy SOLID design.

Detailed Description:
This module contrasts the two primary interface paradigms in Python:
- 'ContractProtocol' establishes an implicit structural contract (Duck Typing).
  Any class implementing the matching method signature is automatically valid.
- 'CloseFromABC' enforces an explicit nominal contract. Even if an unrelated object
  shares the exact same structure, the type checker rejects it without a formal
  subclass relationship.
"""

from typing import Protocol
from abc import ABC


class ContractProtocol(Protocol):
    def close(self) -> None: ...


class ContractABC(ABC):
    def close(self) -> None:
        print("The app is closing from ABC...")


class CloseFromABC(ABC):
    def close(self) -> None:
        print("The app is closing from CloseFromABC...")


class CloseFromProtocol:
    def close(self) -> None:
        print("The app is closing...")


def close_protocol(interface: ContractProtocol):
    interface.close()


def close_abc(interface: CloseFromABC):
    interface.close()


if __name__ == "__main__":
    close_protocol(CloseFromProtocol())  # The app is closing...
    """
    close_abc(CloseFromProtocol())

    Even though both classes possess the "close" method, 
    Pyright flags this as an error. This happens because ABCs 
    enforce nominal typing, meaning explicit inheritance is strictly required.
    """

    close_abc(CloseFromABC())  # The app is closing from CloseFromABC...
