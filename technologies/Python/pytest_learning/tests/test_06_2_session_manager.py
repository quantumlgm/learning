"""
Lesson 06.2: Advanced Fixture Lifecycles, Scopes, and Resource Cleanup.

This test suite covers session connection management, in-memory caching,
and error handling for inactive session operations.

Key Technical Features:
- Fixture Chaining: Demonstrates modular dependency injection (creation -> connection -> data setup).
- Resource Teardown: Uses `yield` statements to ensure automatic session disconnection and cleanup.
- Test Isolation: Prevents side effects across tests through per-function connection state resets.
- Exception Handling: Validates state guardrails using `pytest.raises` for custom and built-in exceptions.
"""

from l_06_2_session_manager import SessionError, SessionManager
import pytest


@pytest.fixture(scope="function")
def create_session():
    session = SessionManager(
        environment="dev",              
    )
    yield session


@pytest.fixture(scope='function')
def connected_session(create_session: SessionManager):
    create_session.connect()
    yield create_session
    create_session.disconnect()


@pytest.fixture
def data_sheet(connected_session: SessionManager):
    connected_session.set_data(key="app", value="Github")
    return connected_session


class TestSessionWork:
    def test_connect(self, create_session: SessionManager):
        create_session.connect()
        assert create_session.is_connected == True

    def test_disconnect(self, create_session: SessionManager):
        create_session.connect()
        create_session.set_data(key="app", value="Github")
        create_session.disconnect()
        assert create_session._cache == {}
        assert create_session.is_connected == False

    def test_set_data(self, data_sheet: SessionManager):   
        assert data_sheet.get_data("app") == "Github"
                
    def test_get_data(self, data_sheet: SessionManager):   
        assert data_sheet.get_data("app") == "Github"

    def test_clear_cache(self, connected_session: SessionManager):
        connected_session.set_data(key="app", value="Github")
        connected_session.clear_cache()
        assert connected_session._cache == {}

    def test_cache_size(self, connected_session: SessionManager):
        connected_session.set_data(key="app", value="Github")
        assert connected_session.cache_size == 1


class TestSessionErrors:
    def test_connect_error(self, connected_session: SessionManager):
        with pytest.raises(SessionError):
            connected_session.connect()

    def test_disconnect_error(self, create_session: SessionManager):        
        with pytest.raises(SessionError):
            create_session.disconnect()        

    def test_set_data_error(self, create_session: SessionManager):   
        with pytest.raises(SessionError):
            create_session.set_data(key='app', value="Github")
                
    def test_get_data_session_error(self, create_session: SessionManager):   
        with pytest.raises(SessionError):
            create_session.get_data("app")

    @pytest.mark.parametrize(
        "check", 
        [
            ("RANDOMKEY@*&#^&@*&#^&@*^*"), 
            ("RANDOMKEY2143435324564"), 
            ("RANDOMKEY;djewnbdefhqe"), 
        ]
    )
    def test_get_data_key_error(self, check: str, connected_session: SessionManager):   
        with pytest.raises(KeyError):
            assert connected_session.get_data(check)



