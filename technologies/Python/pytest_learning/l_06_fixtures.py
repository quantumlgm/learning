"""
Lesson 06.1: Bank Account and Transaction Analytics.

This module provides basic analytics for user bank accounts and transaction history.
It requires pre-configured user profiles and transaction lists to function.
"""

from typing import Literal, TypedDict


class Transaction(TypedDict):
    id: int
    amount: float
    type_: Literal["deposit", "withdrawal"]


class UserProfile(TypedDict):
    user_id: int
    name: str
    is_vip: bool
    balance: float


def calculate_total_balance(profile: UserProfile, transactions: list[Transaction]) -> float:    
    current_balance = profile["balance"]
    
    for tx in transactions:
        if tx["type_"] == "deposit":
            current_balance += tx["amount"]
        elif tx["type_"] == "withdrawal":
            current_balance -= tx["amount"]
            
    return round(current_balance, 2)

def apply_vip_cashback(profile: UserProfile, transactions: list[Transaction]) -> float:    
    if not profile["is_vip"]:
        return 0.0

    total_deposits = sum(tx["amount"] for tx in transactions if tx["type_"] == "deposit")
    return round(total_deposits * 0.05, 2)

print(
    apply_vip_cashback(
        {"user_id": 1, "name": "Ruslan", "is_vip": True, "balance": 1000.0},
        [
            {"id": 1, "amount": 1000.0, "type_": "deposit"},
            {"id": 1, "amount": 500.0, "type_": "withdrawal"},
        ]
))