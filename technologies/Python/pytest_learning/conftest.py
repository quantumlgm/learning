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




"""
FOR NINE LESSON 
"""
def pytest_addoption(parser):
    parser.addoption(
        "--target-env",
        action="store",
        default="dev",
        help="Target environment: dev, stage, or prod"
    )
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="Run slow analytics tests"
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="Pass --run-slow flag to execute this test")
        for item in items:
            if "slow" in item.keywords:
                item.add_marker(skip_slow)


@pytest.fixture(scope="session")
def target_env(request) -> str:
    return request.config.getoption("--target-env")


@pytest.fixture(scope="function")
def report_service(target_env: str) -> ReportService:
    return ReportService(env=target_env)
