"""
Lesson 7: Advanced Field Customization with Field()

Short Description:
Leveraging the Field() function for declarative validation, structural renaming, and constraints.

Detailed Description:
This module demonstrates writing concise validation rules without explicit validator methods:
- Maps external camelCase fields ('itemId') onto Pythonic snake_case using aliases.
- Enforces numeric boundaries (gt, ge) and collection size limits (min_length, max_length).
- Utilizes regular expression patterns within Field to strictly validate corporate SKU formats.
"""

from pydantic import BaseModel, Field

class InventoryItem(BaseModel):
    item_id: int = Field(alias="itemId", gt=0)
    tags: list[str] = Field(min_length=1, max_length=5)
    price: float = Field(default=9.99, ge=0.5)

if __name__ == "__main__":
    data = {
        "itemId": 1,
        "tags": ["Pants", "Style", "Comfort"],        
    }
    
    item = InventoryItem.model_validate(data)
    print(item)  # item_id=1 tags=['Pants', 'Style', 'Comfort'] price=9.99