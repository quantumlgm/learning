"""
Lesson 1: Currency Exchange Core Engine.

This module contains the primary business logic for a retail currency exchange office.
It handles core mathematical conversions, additional service fees for expedited transfers,
and enforces basic input validation rules to protect financial transactions.

Key Business Logic:
- Base Conversion: Calculates the target currency amount based on a provided exchange rate.
- Fast Transfer Service: Adjusts the final payout by applying a flat-rate processing fee.
- Operational Guardrails: Prevents transactions with zero or negative amounts/rates to stop human error.
"""

import time


type num = int | float


def check_transfer(currency: num, exchange_rate: num):
    if currency <= 0 or exchange_rate <= 0:
        raise ValueError(f"The amount of money must not be zero or negative")


def currency_exchange(
    from_valute: str,
    in_valute: str,
    currency: num,
    exchange_rate: num,
):
    time.sleep(1)
    check_transfer(currency, exchange_rate)
    return {
        "in_valute": in_valute,
        "from_valute": from_valute,
        "currency": currency,
        "exchange_rate": exchange_rate,
        "result": currency * exchange_rate,
    }


def fast_conversion(
    from_valute: str,
    in_valute: str,
    currency: num,
    exchange_rate: num,
    extra_charge: num,
):
    check_transfer(currency, exchange_rate)
    return {
        "in_valute": in_valute,
        "from_valute": from_valute,
        "currency": currency,
        "exchange_rate": exchange_rate,
        "result": (currency * exchange_rate) + extra_charge,
    }


print(
    currency_exchange(
        in_valute="USD",
        from_valute="RUB",
        currency=23489.342143,
        exchange_rate=4123541.23451534562124321423453,
    )
)


print(
    fast_conversion(
        in_valute="USD",
        from_valute="RUB",
        currency=200,
        exchange_rate=78.01,
        extra_charge=100,
    )
)
