"""
Lesson 6: Environment Variables and Pydantic Settings

Short Description:
Automating application configuration by loading and validating environment variables from .env files.

Detailed Description:
This module demonstrates the industry-standard approach to Twelve-Factor App configuration:
- Inherits from 'BaseSettings' to leverage automatic environment discovery.
- Integrates 'SettingsConfigDict' to source data from a local '.env' file with strict UTF-8 encoding.
- Automatically handles case-insensitive mapping and type coercion for standard networking types
  (converting string port numbers to native ints, and string flags to actual booleans).
"""

from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    api_host: str
    api_port: int
    secret_key: str
    allow_registration: bool

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


if __name__ == "__main__":
    settings = Settings()
    print(settings.api_port)  # 8000
    print(settings.api_host)  # 127.0.0.1
