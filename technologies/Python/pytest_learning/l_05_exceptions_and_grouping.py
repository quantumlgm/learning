"""
Lesson 05: Credit Scoring and Limit Calculator.

This module evaluates user financial metrics to determine credit eligibility,
assigned credit limit, and interest rates, while raising exceptions for invalid inputs.
"""


def calculate_credit_limit(
    age: int,
    monthly_income: float,
    credit_score: int,
    has_active_defaults: bool = False
) -> dict[str, bool | int | float | str]:
    if age < 18:
        raise ValueError("Client must be at least 18 years old")
    if age > 80:
        raise ValueError("Client age exceeds maximum limit of 80 years")
    if monthly_income < 0:
        raise ValueError("Monthly income cannot be negative")
    if not (300 <= credit_score <= 850):
        raise ValueError("Credit score must be between 300 and 850")

    if has_active_defaults or credit_score < 500:
        return {
            "approved": False,
            "credit_limit": 0.0,
            "interest_rate": 0.0,
            "reason": "High risk client"
        }

    base_limit = monthly_income * 3.0

    if credit_score >= 750:
        multiplier = 1.5
        interest_rate = 12.5
    elif credit_score >= 650:
        multiplier = 1.0
        interest_rate = 17.0
    else:
        multiplier = 0.5
        interest_rate = 24.5

    final_limit = min(base_limit * multiplier, 1_000_000.0)

    return {
        "approved": True,
        "credit_limit": round(final_limit, 2),
        "interest_rate": interest_rate,
        "reason": "Approved"
    }