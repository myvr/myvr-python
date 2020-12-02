import pytest

from myvr.api.exceptions import ResourceUrlError
from myvr.api.resource import APIResource
from tests.utils import API_SOURCE_URL, create_client


class TestApiResource:
    class MyResource(APIResource):
        resource_name = 'MyResource'
        resource_url = 'my-resource'

    @property
    def client(self):
        return create_client()

    @property
    def resource(self):
        return self.MyResource(self.client)

    def test_base_url(self):
        expected_url = API_SOURCE_URL + f'/{self.resource.resource_url}/'
        assert self.resource.base_url == expected_url

    def test_get_key_url(self):
        key = 'key'
        expected_url = API_SOURCE_URL + f'/{self.resource.resource_url}/{key}/'
        assert self.resource.get_key_url(key) == expected_url

    def test_create_resource_with_invalid_api_url(self):
        with pytest.raises(ResourceUrlError):
            class MyResource(APIResource):
                resource_name = 'MyResource'
                resource_url = '/my-resource/'

            MyResource(self.client)

    def test_create_resource_with_invalid_resource_url(self):
        with pytest.raises(ResourceUrlError):
            class MyResource(APIResource):
                resource_name = 'MyResource'
                resource_url = '/my-resource'

            MyResource(self.client)
