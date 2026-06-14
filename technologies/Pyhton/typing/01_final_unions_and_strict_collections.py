"""
Lesson 01: Core Type Hints, Strict Collections, and Type Aliases.

This module demonstrates the fundamentals of Python's static typing ecosystem
using Pyright in strict mode. It covers the application of 'Final' qualifiers
for defining constants, block-level type annotations for primitive types, and
explicit typing for complex structures like sequences (lists, tuples) and
mappings (dictionaries).

Additionally, it showcases the modern Python 3.12+ 'type' statement for
creating explicit Type Aliases, enforcing code legibility, and architectural
safety when dealing with mixed types via Union operators.
"""

from typing import Final

payment_gateway: Final[str] = "GATEWAY_ID"
service_fee: Final[float] = 0.02

# We can use registry: list[Union[str, int]] = []
type Registry = list[str | int]

type TransactionRecord = tuple[str, int | float, str]

type UserWallet = dict[str, int | float]

type ExternalResponse = object

if __name__ == "__main__":
    ruslan: Registry = ["184a754162e24", 200]
    print(ruslan)  # ['184a754162e24', 200]

    ruslan_wallet: UserWallet = {"USD": 1000, "EURO": 200}
    print(ruslan_wallet)  # {'USD': 1000, 'EURO': 200}

    ruslan_transaction: TransactionRecord = ("TXN-2026-06-14", 300, "APPROVED")
    print(ruslan_transaction)  # ('TXN-2026-06-14', 300, 'APPROVED')

    weather_api_respone: ExternalResponse = ["clear_sky", 23.4, "low_solar_activity"]
    if isinstance(weather_api_respone, str):
        print(len(weather_api_respone))
    else:
        print(weather_api_respone)  # ['clear_sky', 23.4, 'low_solar_activity']
