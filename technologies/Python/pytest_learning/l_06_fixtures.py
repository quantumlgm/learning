"""
Lesson 06.1: Bank Account and Transaction Analytics.

This module provides basic analytics for user bank accounts and transaction history.
It requires pre-configured user profiles and transaction lists to function.
"""

from typing import Literal, TypedDict


class Transaction(TypedDict):
    id: str
    amount: float
    type: Literal["deposit", "withdrawal"]


class UserProfile(TypedDict):
    user_id: int
    name: str
    is_vip: bool
    balance: float


def calculate_total_balance(profile: UserProfile, transactions: list[Transaction]) -> float:    
    current_balance = profile["balance"]
    
    for tx in transactions:
        if tx["type"] == "deposit":
            current_balance += tx["amount"]
        elif tx["type"] == "withdrawal":
            current_balance -= tx["amount"]
            
    return round(current_balance, 2)


def apply_vip_cashback(profile: UserProfile, transactions: list[Transaction]) -> float:
    """Calculates total cashback for VIP users (5% on deposits). Non-VIP get 0."""
    if not profile["is_vip"]:
        return 0.0

    total_deposits = sum(tx["amount"] for tx in transactions if tx["type"] == "deposit")
    return round(total_deposits * 0.05, 2)