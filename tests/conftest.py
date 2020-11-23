import pytest

API_URL = 'http://example.com/'
API_KEY = 'test_api_key'
API_VERSION = 'v1'


@pytest.fixture
def api_url():
    return f'{API_URL}{API_VERSION}'
