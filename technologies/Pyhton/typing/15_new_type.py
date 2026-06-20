"""
Lesson 15: NewType and Semantic Subtyping

Short Description:
Creating distinct, zero-overhead semantic types from primitive types using NewType.

Detailed Description:
This module demonstrates how to enforce domain-specific type safety in Python:
- Declares 'TransactionId' and 'UsdAmount' as unique sub-types of 'int' via NewType.
- Prevents accidental logical bugs (like swapping IDs with financial amounts) during static analysis.
- Showcases type-erasure behavior during operations and demonstrates how to re-assert
  the proper semantic type using 'typing.cast'.
"""

from typing import NewType, cast

TransactionID = NewType("TransactionID", int)
AmountUSD = NewType("AmountUSD", int)


def apply_fee(amount: AmountUSD, id: TransactionID) -> str:
    return f"[INFO]: amount - {amount}, id - {id}"


def increase_amount(amount: AmountUSD) -> AmountUSD:
    return cast(AmountUSD, amount + 100)


if __name__ == "__main__":
    transaction = TransactionID(1)
    amount = AmountUSD(200)
    print(
        f"transaction: {transaction}, amount: {amount}"
    )  # transaction: 1, amount: 200

    print(increase_amount(amount))  # 300
    print(apply_fee(amount, transaction))  # [INFO]: amount - 200, id - 1
