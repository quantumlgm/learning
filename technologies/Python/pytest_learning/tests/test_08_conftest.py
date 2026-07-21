"""
Lesson 08: Testing User Management with Centralized Fixtures.

This test suite verifies user repository interactions using shared 
fixtures automatically injected by pytest from conftest.py.
"""

import pytest
from l_08_conftest import UserNotFoundError, UserManager


class TestUserManagerWork:
    def test_add_user(self, user_manager: UserManager):
        user = user_manager.add_user("john_doe", role="admin")
        assert user["username"] == "john_doe"
        assert user["role"] == "admin"
        assert user_manager.count() == 1

    def test_get_existing_user(self, populated_manager: UserManager):
        user = populated_manager.get_user("admin_user")
        assert user["role"] == "admin"
        assert user["active"] is True


class TestUserManagerErrors:
    def test_get_non_existent_user_raises_error(self, user_manager: UserManager):
        with pytest.raises(UserNotFoundError):
            user_manager.get_user("unknown_ghost")