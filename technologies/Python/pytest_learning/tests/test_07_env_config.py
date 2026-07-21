"""
Lesson 07: Testing Environment Variables and Configuration Management.

This test suite validates application configuration loading using both 
pytest-dotenv (.env file integration) and pytest's `monkeypatch` fixture 
for dynamic environment overrides and missing variable scenarios.
"""

import pytest
from l_07_env_config import ConfigurationError, PaymentGatewayConfig


class TestPaymentGatewayWork:
    def test_init_from_env_file(self):
        gateway = PaymentGatewayConfig()
        assert gateway.db_url == "test://test_user:pass@localhost:5432/test_db"
        assert gateway.api_key == "test_secret_key_12345"
        assert gateway.environment == "production"
        assert gateway.timeout == 10
        assert gateway.is_production is True
        assert gateway.get_connection_string() == "test://test_user:pass@localhost:5432/test_db?timeout=10"

    def test_init_defaults(self, monkeypatch):
        monkeypatch.setenv("PAYMENT_DB_URL", "sqlite:///:memory:")
        monkeypatch.setenv("PAYMENT_API_KEY", "default_key")
        monkeypatch.delenv("APP_ENV", raising=False)
        monkeypatch.delenv("GATEWAY_TIMEOUT", raising=False)

        gateway = PaymentGatewayConfig()
        assert gateway.environment == "development"
        assert gateway.timeout == 30
        assert gateway.is_production is False


class TestPaymentGatewayErrors:
    def test_missing_db_url_raises_error(self, monkeypatch):
        monkeypatch.delenv("PAYMENT_DB_URL", raising=False)

        with pytest.raises(ConfigurationError):
            PaymentGatewayConfig()

    def test_missing_api_key_raises_error(self, monkeypatch):
        monkeypatch.delenv("PAYMENT_API_KEY", raising=False)

        with pytest.raises(ConfigurationError):
            PaymentGatewayConfig()
