from dataclasses import dataclass, field
import uuid


def generate_hero_id():
    return uuid.uuid4()


@dataclass
class BaseVault:
    name: str
    hp: int = field(default=100)
    id: str = field(default_factory=generate_hero_id())

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
    swordsman = Hero('Geralt of Rivia', 60, 100)
    print(swordsman) # Hero(name='Geralt of Rivia', hp=60, id=100, level=1, mana=50)

    bounty_hunter = Hero('Leo Bonhart', 100, 50, 50)
    print(bounty_hunter) # Hero(name='Geralt of Rivia', hp=100, id=50, level=50, mana=100)