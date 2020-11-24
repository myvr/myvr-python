import pytest

API_URL = 'http://example.com/'
API_KEY = 'test_api_key'
API_VERSION = 'v1'


@pytest.fixture
def api_url():
    return f'{API_URL}{API_VERSION}'


@pytest.fixture
def resource_data():
    return {
        'key': 'test_key',
        'name': 'test_name'
    }


@pytest.fixture
def resource_list_data():
    return {
        'results': [
            {'key': 'key1', 'name': 'name1'},
            {'key': 'key2', 'name': 'name2'}
        ],
        'limit': 0,
        'offset': 5,
        'count': 2
    }
