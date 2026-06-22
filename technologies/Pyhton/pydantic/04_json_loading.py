"""
Lesson 4: Creating Pydantic Models from JSON Files

Short Description:
Deserializing and validating raw JSON text directly into structured Pydantic objects.

Detailed Description:
This module demonstrates integration with external data sources using JSON:
- Establishes a 'GoodCard' schema representing warehouse product inventory status.
- Implements Python's context manager ('with open') to safely stream file contents from disk.
- Utilizes the high-performance 'model_validate_json()' method to parse raw text and 
  automatically coerce string-formatted inputs into their respective Python types (int, bool).
"""

from pydantic import BaseModel

class GoodCard(BaseModel):
    product_name: str
    stock_count: int
    available: bool
    discount_percentage: float = 0.0

if __name__ == "__main__":
    with open("04_data.json", "r", encoding="utf-8") as file:
        text = file.read()

    data = GoodCard.model_validate_json(text)
    print(data) # product_name='Pro Gaming Keyboard' stock_count=45 available=True discount_percentage=15.5
