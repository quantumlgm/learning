"""
Lesson 08: Generic Functions and Type Parameters (Python 3.12+)

Short Description:
A collection of generic utilities demonstrating type safety and dynamic type
preservation using modern PEP 695 syntax.

Detailed Description:
This module showcases advanced static typing features in contemporary Python:
- Explicit type parameter syntax '[T]' to create fully generic components.
- Multi-parameter generic signatures linking disparate input types to precise
  tuple structures.
- Type constraints limiting generics to specified primitives, preventing
  type dilution (e.g., preserving literal 'int' or 'float' behaviors).
"""


def get_first_item[T](values: list[T]) -> T:
    return values[0]


def get_both[T, Y](one: T, two: Y) -> tuple[T, Y]:
    return (one, two)


def get_doubled[T: (int, float)](value: T) -> T:
    return value * 2


if __name__ == "__main__":
    print(get_first_item(["Quan", "tum", "lgm"]))  # Quan
    print(get_both("Hello", 1001))  # ('Hello', 1001)
    print(get_doubled(5))  # 10
