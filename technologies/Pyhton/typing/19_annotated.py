"""
Lesson 19: Annotated and Metadata Introspection

Short Description:
Attaching runtime metadata to types using Annotated and inspecting it via typing tools.

Detailed Description:
This module demonstrates the foundation of modern validation frameworks (like Pydantic):
- Uses 'Annotated' to pair a primitive type (int) with a custom metadata class (ValueRange).
- Leverages 'get_type_hints' with 'include_extras=True' to prevent metadata erasure.
- Uses 'get_args' to unpack the metadata object at runtime and enforce boundaries dynamically, 
  all while keeping static type checkers completely satisfied.
"""

from dataclasses import dataclass
from typing import Annotated, get_args, get_type_hints

@dataclass
class ValueRange:
    min_val: int
    max_val: int

Valid = Annotated[int, ValueRange(0, 100)]

def validate_args(arg: Valid):
    hints = get_type_hints(validate_args, include_extras=True)    
    my_type = hints["arg"]

    args = get_args(my_type)    
    settings = args[1]
    if not (settings.min_val <= arg <= settings.max_val):
        raise ValueError(f"Value {arg} out of range [{settings.min_val}, {settings.max_val}]")
    print(arg)

if __name__ == '__main__':    
    validate_args(100) # 100
    validate_args(200)  # ValueError: Value 200 out of range [0, 100]
        