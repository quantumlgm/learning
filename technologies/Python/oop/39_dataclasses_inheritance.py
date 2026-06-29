"""
Task 39: Data Classes Inheritance and Advanced Field Factories.

This program concludes the OOP course by demonstrating how data classes 
behave under inheritance, focusing on field ordering and post-init execution.

Key Features:
- Metamethod Chaining: Correctly utilizes super().__post_init__() inside the 
  derived 'Hero' class to ensure parent initialization logic is executed first.
- Explicit Keyword Arguments: Instantiates subclasses using named arguments 
  to prevent parameter mismatch caused by dataclass inheritance field ordering.
- Dynamic Default Factories: Passes a callable reference (generate_hero_id) 
  to 'default_factory' to ensure a fresh, unique string UUID for each instance.
- Conditional Property Mutation: Dynamically modifies subclass attributes (mana scaling) 
  based on state evaluation (hero level) during the post-init phase.
"""


from dataclasses import dataclass, field
import uuid


def generate_hero_id():
    return str(uuid.uuid4())


@dataclass
class BaseVault:
    name: str
    hp: int = field(default=100)
    id: str = field(default_factory=generate_hero_id, repr=False)

    def __post_init__(self):
        if self.hp <= 0:
            self.hp = 1


@dataclass
class Hero(BaseVault):
    level: int = 1
    mana: int = 50

    def __post_init__(self):
        super().__post_init__()
        if self.level > 10:
            self.mana = self.mana * 2


if __name__ == "__main__":
    swordsman = Hero("Geralt of Rivia", hp=60, level=100)
    print(swordsman)  # Hero(name='Geralt of Rivia', hp=60, level=100, mana=100)

    bounty_hunter = Hero("Leo Bonhart", hp=100, level=50, mana=50)
    print(bounty_hunter)  # Hero(name='Leo Bonhart', hp=100, level=50, mana=100)
