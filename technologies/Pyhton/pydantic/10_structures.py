"""
Lesson 10: Model Inheritance and Composition

Short Description:
Structuring complex data schemas using object-oriented inheritance and nested model composition.

Detailed Description:
This module demonstrates the synthesis of data structural design patterns in Pydantic V2:
- Implements Model Inheritance (UserOut extends UserBase) to share and extend core attributes.
- Implements Model Composition by nesting the 'Address' model inside 'UserOut' to represent hierarchical data.
- Validates a deeply nested dictionary payload into fully realized typed objects via '.model_validate()'.
"""

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    street: str

class UserBase(BaseModel):
    username: str
    email: str

class UserOut(UserBase):
    id: int
    address: Address

if __name__ == "__main__":
    user_info = {
    "username": "python_quantum",
    "email": "quantum@python.org",
    "id": 99,
    "address": {
        "city": "Astana",
        "street": "Mangilik El"
        }
    }
    data = UserOut.model_validate(user_info)