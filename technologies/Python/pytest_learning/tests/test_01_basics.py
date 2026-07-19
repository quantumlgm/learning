"""
Lesson 1: Pytest Discovery, Basic Assertions, and Test Execution Flow.

This test suite introduces the fundamentals of testing Python applications using Pytest,
focusing on test discovery rules, assertion evaluation, and mathematical correctness.

Key Technical Features:
- Test Discovery Mechanics: Demonstrates how Pytest automatically detects test files 
  and test functions using specific naming conventions (`test_*`).
- State and Dictionary Verification: Validates functional correctness by verifying keys, 
  data types, and structure alignment in returned dictionaries.
- Float Precision Handling: Examines how standard assertions interact with Python's floating-point 
  arithmetic precision limitations (IEEE 754) during complex multiplication.
"""


from l_01_basics import currency_exchange, fast_conversion


def test_currency_exchange_properly():
    result = currency_exchange(
        in_valute='USD', 
        from_valute='RUB',
        currency=100,
        exchange_rate=78.28
    )
    assert result["in_valute"] == 'USD'
    assert result["from_valute"] == "RUB"
    assert result["currency"] == 100
    assert result["exchange_rate"] == 78.28    

    assert result["result"] == 7828.0

def test_fast_conversion_properly():
    result = fast_conversion(
        in_valute='USD', 
        from_valute='RUB',
        currency=200,
        exchange_rate=78.01,
        extra_charge=100
    )   
    assert result["in_valute"] == 'USD'
    assert result["from_valute"] == "RUB"
    assert result["currency"] == 200
    assert result["exchange_rate"] == 78.01
    assert result["extra_charge"] == 100

    assert result["result"] == 15702.000000000002


def test_check_all_results():
    result = currency_exchange(
        in_valute='USD', 
        from_valute='RUB',
        currency=70,
        exchange_rate=0.5
    ) 
    assert result["result"] == 35.0

    result = currency_exchange(
        in_valute='USD', 
        from_valute='RUB',
        currency=23489.342143,
        exchange_rate=4123541.23451534562124321423453
    ) 
    assert result["result"] == 96859270898.29956

    result = currency_exchange(
        in_valute='USD', 
        from_valute='RUB',
        currency=2,
        exchange_rate=10
    ) 
    assert result["result"] == 20

