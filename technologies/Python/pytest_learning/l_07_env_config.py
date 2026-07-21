"""
Lesson 07: Managing Application Configuration via Environment Variables.

This module loads database connection strings, API credentials, and application 
run modes directly from environment variables. It enforces validation for required 
keys and provides fallback values for optional flags.
"""

import os


class ConfigurationError(ValueError):
    pass


class PaymentGatewayConfig:
    def __init__(self):
        self.db_url = self._get_required_env("PAYMENT_DB_URL")
        self.api_key = self._get_required_env("PAYMENT_API_KEY")
        self.environment = os.getenv("APP_ENV", "development")
        self.timeout = int(os.getenv("GATEWAY_TIMEOUT", "30"))

    def _get_required_env(self, key: str) -> str:
        value = os.getenv(key)
        if not value:
            raise ConfigurationError(f"Missing required environment variable: {key}")
        return value

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"

    def get_connection_string(self) -> str:
        return f"{self.db_url}?timeout={self.timeout}"