"""
In-memory session manager and key-value cache for test automation.

Provides session lifecycle handling with active connection states.
Used to demonstrate Pytest fixture lifecycles, teardown, and autouse resets.
"""

from typing import Any


class SessionError(Exception):
    pass


class SessionManager:
    def __init__(self, environment: str) -> None:
        self.environment = environment
        self.is_connected = False
        self._cache: dict[str, Any] = {}

    def connect(self) -> None:
        if self.is_connected:
            raise SessionError("Session is already connected.")
        self.is_connected = True

    def disconnect(self) -> None:
        if not self.is_connected:
            raise SessionError("Cannot disconnect an inactive session.")
        self.is_connected = False
        self._cache.clear()

    def set_data(self, key: str, value: Any) -> None:
        if not self.is_connected:
            raise SessionError("Cannot write data to an inactive session.")
        self._cache[key] = value

    def get_data(self, key: str) -> Any:
        if not self.is_connected:
            raise SessionError("Cannot read data from an inactive session.")
        if key not in self._cache:
            raise KeyError(f"Key '{key}' not found in cache.")
        return self._cache[key]

    def clear_cache(self) -> None:
        self._cache.clear()

    @property
    def cache_size(self) -> int:
        return len(self._cache)