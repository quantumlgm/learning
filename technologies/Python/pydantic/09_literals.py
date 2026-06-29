"""
Lesson 9: Strict Value Validation with Literal Types

Short Description:
Restricting field inputs to a predefined set of exact values using Python's typing.Literal.

Detailed Description:
This module demonstrates how to enforce strict domain-specific choices at the type level:
- Replaces generic string/integer types with precise 'Literal' definitions for statuses and methods.
- Eliminates the need for custom choice-checking validators by leveraging built-in type constraints.
- Validates that fields perfectly match defined literal elements during '.model_validate()' processing.
"""

from pydantic import BaseModel
from typing import Literal, Annotated

DeliveryMethod = Literal["ground", "air", "sea"]
PackageStatus = Annotated[str, Literal["in_transit", "retained", "delivered"]]


class DeliveryTask(BaseModel):
    track_id: int
    method: DeliveryMethod
    status: PackageStatus
    priority_level: Literal[1, 2, 3]


if __name__ == "__main__":
    info = {
        "track_id": 1,
        "method": "ground",
        "status": "retained",
        "priority_level": 1,
    }
    data = DeliveryTask.model_validate(info)
    print(data)  # track_id=1 method='ground' status='retained' priority_level=1
