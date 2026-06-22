"""
Lesson 8: Reusable Types via Annotated and Field

Short Description:
Creating custom, reusable data types with embedded Pydantic validation rules.

Detailed Description:
This module demonstrates code reuse and adherence to the DRY principle in Pydantic V2:
- Defines module-level type aliases ('TransactionId', 'CurrencyAmount') using 'typing.Annotated'.
- Encapsulates regex patterns and numeric/string constraints directly within type metadata.
- Demonstrates how Pydantic shields field declarations from verbose inline configuration.
"""

from pydantic import Field, BaseModel
from typing import Annotated

TransactionId = Annotated[str, Field(pattern=r"^TX-\d{5}$")]
CurrencyAmount = Annotated[float, Field(gt=0)]
PaymentDescription = Annotated[str, Field(min_length=5, max_length=100)]

class Invoice(BaseModel):
    invoice_id: TransactionId
    amount: CurrencyAmount
    description: PaymentDescription

if __name__ == "__main__":
    payment_info = {
        "invoice_id": "TX-12345",
        "amount": 3.22,
        "description": "Moon ticket purchase successful now"
        
    }
    payment_data = Invoice.model_validate(payment_info)
    print(payment_data) # invoice_id='TX-12345' amount=3.22 description='Moon ticket purchase successful now'