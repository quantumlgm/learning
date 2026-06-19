"""
Lesson 12: Advanced Protocols and the Template Method Pattern

Short Description:
An implementation of the behavioral Template Method design pattern using
a hybrid Protocol approach with abstract and final methods.

Detailed Description:
This module demonstrates how protocols can act as base blueprints with concrete logic:
- 'Template' protocol defines a strict algorithmic skeleton via '@final'.
- It forces implementations to supply specific behavioral hooks using '@abstractmethod'.
- 'Stepper' explicitly inherits from the protocol to reuse the concrete execution skeleton.
- Showcases static protection against overriding final methods and explicit container
  type inference for list collections.
"""

from typing import Protocol, final
from abc import abstractmethod


class Template(Protocol):
    @abstractmethod
    def step(self) -> str: ...

    @final
    def step_algorithm(self):
        print("Program is starting")
        print(f"Result of the function: {self.step()}")
        print("Program has ended!")


class Stepper(Template):
    def step(self) -> str:
        return "Hello! My name is Stepper!"


"""
class Mistaker(Template):
    def step_algorithm(self): <---- Pyright gives us an error because
        print("It'll be mistake!")  this function is protected in parent class
"""


def receiver(values: list[Template]):
    for v in values:
        print(v.step())


if __name__ == "__main__":
    objects: list[Template] = []
    objects.extend([Stepper(), Stepper()])
    print(objects)  # [<__main__.Stepper object at 0x0000020AAAAA6870>]

    receiver(objects)  # Hello! My name is Stepper!
                       # Hello! My name is Stepper!
