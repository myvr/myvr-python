import pytest


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


@pytest.fixture
def key():
    return 'key'
