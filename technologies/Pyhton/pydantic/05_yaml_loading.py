"""
Lesson 5: Parsing Hierarchical YAML Configurations

Short Description:
Deserializing nested YAML structures into strongly-typed nested Pydantic models.

Detailed Description:
This module demonstrates advanced configuration management via third-party parsers:
- Utilizes 'pyyaml' (yaml.safe_load) to securely map YAML strings onto native Python dicts.
- Illustrates object composition by embedding the 'SecuritySettings' model inside 'ServerConfig'.
- Employs 'model_validate()' to validate and construct a deeply nested, immutable config tree.
"""

from pydantic import BaseModel
import yaml

class Settings(BaseModel):
    enable_firewall: bool
    allowed_attempts: int

class Config(BaseModel):
    server_name: str
    max_players: int
    protection: Settings

if __name__ == "__main__":
    with open("05_config.yaml") as file:
        text = yaml.safe_load(file)

    data = Config.model_validate(text)
