import pytest

from l_04_parametrize import calculate_subscription_price

@pytest.mark.parametrize(
    "tier, months, promo_code, with_mentor, check",
    [
        ("basic", 2, "SUMMER2026", True, {
            "expected_base": 2000.0, 
            "expected_applied": 0.2, 
            "expected_mentor": 3000.0, 
            "expected_total": 4600.0
        }),

        ("basic", 2, None, True, {
            "expected_base": 2000.0, 
            "expected_applied": 0.0, 
            "expected_mentor": 3000.0, 
            "expected_total": 5000.0
        }),

        ("basic", 2, "SUMMER2026", False, {
            "expected_base": 2000.0, 
            "expected_applied": 0.2, 
            "expected_mentor": 0.0, 
            "expected_total": 1600.0
        }),

        ("basic", 2, "WELCOME10", True, {
            "expected_base": 2000.0, 
            "expected_applied": 0.1, 
            "expected_mentor": 3000.0, 
            "expected_total": 4800.0
        }),

        ("basic", 13, "SUMMER2026", True, {
            "expected_base": 13000.0, 
            "expected_applied": 0.2, 
            "expected_mentor": 19500.0,
            "expected_total": 29900.0
        }),
    ]
)
def test_calculate_subscription_price(
    tier: str,
    months: int,
    promo_code: str | None,
    with_mentor: bool,
    check: dict[str, int | float],
):
    res = calculate_subscription_price(
        tier, months, promo_code, with_mentor
    )
    assert res["base_price"] == check["expected_base"]
    assert res["discount_applied"] == check["expected_applied"]
    assert res["mentor_fee"] == check["expected_mentor"]
    assert res["total_price"] == check["expected_total"]
    
