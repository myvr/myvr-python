import pytest

from myvr.api.exceptions import ResourceUrlError
from myvr.api.resource import APIResource
from tests.utils import API_SOURCE_URL, create_client


class TestApiResource:
    class MyResource(APIResource):
        name = 'MyResource'
        path = 'my-resource'

    @property
    def client(self):
        return create_client()

    @property
    def resource(self):
        return self.MyResource(self.client)

    def test_base_url(self):
        expected_url = API_SOURCE_URL + f'/{self.resource.path}/'
        assert self.resource.base_url == expected_url

    def test_add_path(self):
        key = 'key'
        path = 'path'
        expected_url = API_SOURCE_URL + f'/{self.resource.path}/{key}/{path}/'
        actual_url = self.resource.add_path(self.resource.base_url, key, path)
        assert actual_url == expected_url

    def test_create_resource_with_invalid_api_url(self):
        with pytest.raises(ResourceUrlError):
            class MyResource(APIResource):
                name = 'MyResource'
                path = '/my-resource/'

            MyResource(self.client)

    def test_create_resource_with_invalid_resource_url(self):
        with pytest.raises(ResourceUrlError):
            class MyResource(APIResource):
                name = 'MyResource'
                path = '/my-resource'

            MyResource(self.client)

    def test_action(self, requests_mock):
        path = 'test-path'
        full_url = API_SOURCE_URL + f'/{self.resource.path}/{path}/'

        requests_mock.post(full_url, text='{}')

        response = self.resource.action(path)
        assert response == {}

    def test_object_action(self, requests_mock):
        key = 'key'
        path = 'path'
        full_url = API_SOURCE_URL + f'/{self.resource.path}/{key}/{path}/'

        requests_mock.post(full_url, text='{}')

        response = self.resource.object_action(key, path, 'POST')
        assert response == {}
