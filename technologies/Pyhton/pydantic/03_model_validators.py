"""
Lesson 3: Pydantic Model Validators (Multi-field Business Logic)

Short Description:
Enforcing model-level constraints across multiple interdependent fields using @model_validator.

Detailed Description:
This module demonstrates advanced validation where business rules rely on a combination of fields:
- Uses 'Literal' to restrict the allowed hotel room categories.
- Implements '@model_validator(mode="after")' operating on the 'self' instance post-field-validation.
- Validates conditional matrix logic: guarantees SPA access for 'Suite' rooms, enforces upper price 
  caps for 'Comfort' rooms, and maintains a minimum price floor for 'Standard' rooms.
"""

from __future__ import annotations
from pydantic import BaseModel, model_validator
from typing import Literal

class Booking(BaseModel):
    room: Literal["Standard", "Suite", "Comfort"]
    has_spa: bool
    night_price: float

    @model_validator(mode="after")
    def model_checker(self) -> Booking: 
        if self.room == "Suite":
            if self.has_spa == False:
                raise ValueError("A suite room must have spa access")
        elif self.room == "Comfort":
            if self.night_price > 1000:
                raise ValueError("A comfort room must be less than 1000")    
        elif self.room == "Standard":
            if self.night_price < 200:
                raise ValueError("A standard room must be greater than 200")    
        return self
    

if __name__ == "__main__":
    suite_booking = Booking(room="Suite", has_spa=True, night_price=200)
    print(suite_booking) # room='Suite' has_spa=True night_price=200.0

    try:
        comfort_booking = Booking(room="Comfort", has_spa=True, night_price=2000)
    except ValueError:
        print("A comfort room must be less then 1000") # A comfort room must be less then 1000
        