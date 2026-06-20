from typing import NewType, cast

TransactionID = NewType("TransactionID", int)
AmountUSD = NewType("AmountUSD", int)

def apply_fee(amount: AmountUSD, id: TransactionID) -> str:
    return f"[INFO]: amount - {amount}, id - {id}"

def increase_amount(amount: AmountUSD) -> AmountUSD:
    return cast(AmountUSD, amount + 100)

if __name__ == "__main__":
    transaction = TransactionID(1)
    amount = AmountUSD(200)
    print(f"transaction: {transaction}, amount: {amount}")  # transaction: 1, amount: 200
    
    print(increase_amount(amount)) # 300
    print(apply_fee(amount, transaction)) # [INFO]: amount - 200, id - 1