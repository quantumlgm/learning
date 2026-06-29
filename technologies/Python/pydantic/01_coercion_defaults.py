"""
Lesson 1: Pydantic Basic Models, Coercion, and Defaults

Short Description:
Declaring fields, observing type coercion, and setting up optional vs. required parameters.

Detailed Description:
This module demonstrates the foundation of Pydantic data validation:
- Defines a 'PlayerProfile' inheriting from 'BaseModel' with specific type constraints.
- Proves 'Type Coercion' by passing an integer (1) to a boolean field, which Pydantic normalizes.
- Clarifies the strict difference between an explicit required field allowing None
  ('guild_tag: str | None') and a truly optional field with a default fallback ('biography').
- Shows data serialization using the native '.model_dump()' method.
"""

from pydantic import BaseModel
from pprint import pprint


class PlayerProfile(BaseModel):
    player_id: int
    username: str
    is_premium: bool = False
    guild_tag: str | None
    biography: str | None = None


if __name__ == "__main__":
    player = PlayerProfile(player_id=1, username="Gamer", is_premium=1, guild_tag=None)
    """
    Even though our linter will report an error, the type conversion 
    will work and convert the number 1 to a boolean.
    """

    pprint(player.model_dump())
    """
    {'biography': None,
    'guild_tag': None,
    'is_premium': True,
    'player_id': 1,
    'username': 'Gamer'}
    """
