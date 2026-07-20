""""
Lesson 06.1: Basic Pytest Fixtures and Dependency Injection.

This test suite verifies bank account balance calculations and VIP cashback processing.
It demonstrates explicit fixture usage to provide isolated, clean test environments.

Key Technical Features:
- Atomic Fixtures: Reusable `@pytest.fixture` definitions returning distinct user profiles and transaction sets.
- Dependency Injection: Implicit context delivery to test functions via parameter signature naming.
- Clean Test Separation: Isolates regular vs. VIP customer logic without code duplication.
"""

import pytest
from l_06_fixtures import calculate_total_balance, apply_vip_cashback, Transaction, UserProfile


@pytest.fixture
def regular_user():
    return {"user_id": 1, "name": "Ruslan", "is_vip": False, "balance": 1000.0}


@pytest.fixture
def vip_user():
    return {"user_id": 1, "name": "Ruslan", "is_vip": True, "balance": 1000.0}


@pytest.fixture
def sample_transactions():
    return [
        {"id": "1", "amount": 1000.0, "type_": "deposit"},
        {"id": "2", "amount": 500.0, "type_": "withdrawal"},
    ]


def test_calculate_total_balance_regular(regular_user: UserProfile, sample_transactions: list[Transaction]):
    res = calculate_total_balance(regular_user, sample_transactions)
    assert res == 1500.0


def test_calculate_total_balance_vip(vip_user: UserProfile, sample_transactions: list[Transaction]):
    res = calculate_total_balance(vip_user, sample_transactions)
    assert res == 1500.0


def test_apply_vip_cashback_regular(regular_user: UserProfile, sample_transactions: list[Transaction]):
    res = apply_vip_cashback(regular_user, sample_transactions)
    assert res == 0


def test_apply_vip_cashback_vip(vip_user: UserProfile, sample_transactions: list[Transaction]):
    res = apply_vip_cashback(vip_user, sample_transactions)
    assert res == 50.0