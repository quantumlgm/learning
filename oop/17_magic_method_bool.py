# Design a class named `PlayerProfile` that evaluates the truth value
# (truthiness) of its instances using the `__bool__` magic
# method based on the player's status.

# Requirements:
# 1. Initialization:
#    - Accepts `nickname` (str), `health` (int, 0 to 100), and an
#      optional `is_banned` (bool, defaults to False).

# 2. Magic Methods:
#    - Implement `__bool__`: A player profile is considered truthy
#      (`True`) if and only if their `health` is strictly greater
#      than 0 AND `is_banned` is `False`. If the player is dead (health == 0)
#      or banned, it must return `False`.
#    - Implement `__len__`: Returns the player's current health value.
#      This allows the object to be used in numeric contexts where
#      length/health representation is required.


class PlayerProfile:
    def __init__(self, nickname: str, health: int, is_banned: bool = False) -> None:
        self.nickname = nickname
        self.health = health
        self.is_banned = is_banned

    def __bool__(self) -> bool:
        return self.health > 0 and not self.is_banned

    def __len__(self):
        return self.health


if __name__ == "__main__":
    Player = PlayerProfile("Quantum", 90)
    print(bool(Player))  # True
    Player.health = 0
    print(len(Player))  # 0
    print(bool(Player))  # False
    Player.health = 90
    Player.is_banned = True
    print(bool(Player))  # False
    print(len(Player))  # 90

    if Player:
        print("Everything is good")
    else:
        print("Something is bad") # Something is bad
