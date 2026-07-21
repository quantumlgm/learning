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



