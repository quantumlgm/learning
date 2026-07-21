"""
Lesson 08: Modularity with conftest.py and Fixture Scopes.

This module models an in-memory user repository simulating user creation,
retrieval, and authentication checks against a isolated user database.
"""


class UserNotFoundError(Exception):
    pass


class UserManager:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self._users = {}

    def add_user(self, username: str, role: str = "user") -> dict:
        user_data = {"username": username, "role": role, "active": True}
        self._users[username] = user_data
        return user_data

    def get_user(self, username: str) -> dict:
        if username not in self._users:
            raise UserNotFoundError(f"User {username} not found in {self.db_name}")
        return self._users[username]

    def count(self) -> int:
        return len(self._users)