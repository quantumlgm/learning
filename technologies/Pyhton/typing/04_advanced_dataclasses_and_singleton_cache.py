"""
Lesson 04: Advanced Dataclasses and Singleton Cache

Short Description:
A lightweight FinTech transaction module featuring immutable data models,
modern type aliases, and a strict Singleton cache with a fluent interface.

Detailed Description:
This module demonstrates advanced Python 3.12+ object-oriented and typing patterns:
- 'TransactionData' is a frozen dataclass ensuring post-creation immutability,
  using a dynamic field factory to safely handle mutable default tags.
- 'Status' utilizes the modern 'type' syntax and pipe (|) operator for clean union types.
- 'Cash' implements the Singleton pattern via '__new__' to centralize in-memory storage,
  blocks inheritance with '@final', tracks global state using 'ClassVar', and enables
  method chaining by returning 'Self'.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import final, ClassVar, Self


type Status = str | int


@dataclass(frozen=True)
class TransactionData:
    id: int
    amount: float
    status: Status
    tags: list[str] = field(default_factory=list[str])


@final
class Cash:
    _instance: ClassVar[Cash | None] = None
    operations_count: ClassVar[int] = 0

    def __new__(cls) -> Cash:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "transactions"):
            self.transactions: list[TransactionData] = []

    def save(self, transaction: TransactionData) -> Self:
        self.transactions.append(transaction)
        Cash.operations_count += 1
        return self


if __name__ == "__main__":
    tx1 = TransactionData(
        id=101, amount=250.50, status="processed", tags=["gamedev", "premium"]
    )
    tx2 = TransactionData(id=102, amount=15.00, status="rejected", tags=["food"])
    print(tx2)  # TransactionData(id=102, amount=15.0, status='rejected', tags=['food'])

    tx3 = TransactionData(id=103, amount=1000.00, status="pending")
    print(tx3)  # TransactionData(id=103, amount=1000.0, status='pending', tags=[])

    cache_1 = Cash()
    cache_2 = Cash()
    cache_1.save(tx1)
    print(cache_1.transactions)
