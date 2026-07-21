"""
Shared test configuration and global fixtures.
"""

import pytest
from l_08_conftest import UserManager


@pytest.fixture(scope="function")
def user_manager():
    manager = UserManager(db_name="test_db")
    yield manager


@pytest.fixture(scope="function")
def populated_manager(user_manager: UserManager):    
    user_manager.add_user("admin_user", role="admin")
    user_manager.add_user("standard_user", role="user")
    return user_manager