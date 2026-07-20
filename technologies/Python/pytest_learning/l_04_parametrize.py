"""
Lesson 04: Subscription Engine.

This module handles calculation of subscription prices for an edtech platform.
It processes different tiers, applies promotional discounts, and adds charges
for extra features like personal mentorship or extended access.
"""


def calculate_subscription_price(
    tier: str, months: int, promo_code: str | None = None, with_mentor: bool = False
) -> dict[str, str | int | float]:
    prices = {"basic": 1000.0, "standard": 2500.0, "premium": 5000.0}

    if tier not in prices:
        raise ValueError(f"Unknown subscription tier: {tier}")

    if months <= 0:
        raise ValueError("Subscription period must be at least 1 month")

    base_price = prices[tier] * months
    discount = 0.0

    if promo_code == "SUMMER2026":
        discount = 0.20
    elif promo_code == "WELCOME10":
        discount = 0.10

    if months >= 12 and promo_code != "SUMMER2026":
        discount = max(discount, 0.15)

    discounted_price = base_price * (1 - discount)

    mentor_fee = 1500.0 * months if with_mentor else 0.0
    total_price = discounted_price + mentor_fee

    return {
        "tier": tier,
        "months": months,
        "base_price": base_price,
        "discount_applied": discount,
        "mentor_fee": mentor_fee,
        "total_price": total_price,
    }
