"""
Lesson 16: TypeIs and Two-Way Type Narrowing

Short Description:
Implementing dual-branch type narrowing using TypeIs predicates from typing_extensions.

Detailed Description:
This module demonstrates the practical difference between TypeGuard and TypeIs:
- Implements an 'is_string' predicate function that asserts a 'str' type on True.
- Showcases how TypeIs performs set-theoretic subtraction on the False branch.
- Validates that Pyright correctly narrows the type to 'int' in the 'else' block,
  allowing arithmetic operations without explicit runtime isinstance checks.
"""

from typing_extensions import TypeIs
from typing import TypeGuard


def check_is(value: str | int) -> TypeIs[str]:
    return isinstance(value, str)


def check_guard(value: str | int) -> TypeGuard[str]:
    return isinstance(value, str)


def processing_is(data: str | int):
    if check_is(data):
        return data.upper()
    else:
        return data + 10


def processing_guard(data: str):
    if check_guard(data):
        return f"[VERIFY]: String {data} passed the inspection"
    else:
        return data


if __name__ == "__main__":
    print(processing_is("String"))  # STRING
    print(processing_is(10))  # 20

    print(processing_guard("String"))  # [VERIFY]: String String passed the inspection

    """
    print(processing_guard(10)) 
    If we use it and also write

19  else:
20      return data 

    we recieve the pyright error 
    that tell about data can be any type 
    """
