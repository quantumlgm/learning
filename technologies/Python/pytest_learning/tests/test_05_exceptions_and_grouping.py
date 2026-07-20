import pytest

from l_05_exceptions_and_grouping import calculate_credit_limit

class TestCalculateCreditLimit:
    @pytest.mark.parametrize(
        "age, monthly_income, credit_score, has_active_defaults, check",
        [
            (20, 1300.0, 600, False, {
                "approved": True, 
                "credit_limit": 1950.0, 
                "interest_rate": 24.5, 
                "reason": "Approved"
            }),
            (20, 1300.0, 850, False, {
                "approved": True, 
                "credit_limit": 5850.0, 
                "interest_rate": 12.5, 
                "reason": "Approved"
            }),
            (20, 1300.0, 400, False, {
                "approved": False, 
                "credit_limit": 0.0, 
                "interest_rate": 0.0, 
                "reason": "High risk client"
            }),
        ]
        
    )
    def test_calculate_success(
        self,
        age: int, 
        monthly_income: float, 
        credit_score: int, 
        has_active_defaults: bool,
        check: dict[str, int | float | str]
    ):
        res = calculate_credit_limit(age, monthly_income, credit_score, has_active_defaults)
        assert check["approved"] == res["approved"]
        assert check["credit_limit"] == res["credit_limit"]
        assert check["interest_rate"] == res["interest_rate"]
        assert check["reason"] == res["reason"]


    @pytest.mark.parametrize(
        "age, monthly_income, credit_score, has_active_defaults",
        [
            (10, 1300.0, 600, False),
            (90, 1300.0, 600, False),
            (20, -1000, 600, False),
            (20, 1200, 200, False),
            (20, 1300.0, 0, False),                                   
        ]
        
    )
    def test_calculate_error(
        self,
        age: int, 
        monthly_income: float, 
        credit_score: int, 
        has_active_defaults: bool,        
    ):
        with pytest.raises(ValueError):
            calculate_credit_limit(age, monthly_income, credit_score, has_active_defaults)

