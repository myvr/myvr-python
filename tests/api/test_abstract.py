import json

import pytest
import requests_mock

from myvr.api.abstract import APIResource, CreateMixin, DeleteMixin, ListMixin, UpdateMixin
from myvr.api.exceptions import ResourceUrlError
from myvr.api.myvr_objects import MyVRCollection, MyVRObject
from tests.conftest import API_KEY, API_URL, API_VERSION


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


class TestApiResource:
    class MyResource(APIResource):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    @property
    def resource(self):
        return self.MyResource(API_KEY, API_URL, API_VERSION)

    def test_retrieve(self, api_url, resource_data):
        with requests_mock.Mocker() as m:
            resource_url = f"{api_url}{self.MyResource.resource_url}{resource_data['key']}/"

            m.get(resource_url, text=json.dumps(resource_data))
            res = self.resource.retrieve(resource_data['key'])

            assert isinstance(res, MyVRObject)
            assert res.key == resource_data['key']

    def test_get_headers(self):
        headers = {}
        actual_headers = self.resource.get_headers(headers)
        expected_headers = {
            'Authorization': f'Bearer {API_KEY}'
        }
        assert actual_headers == expected_headers

    def test_get_headers_with_other_headers(self):
        headers = {
            'head1': 'head1',
        }
        actual_headers = self.resource.get_headers(headers)
        expected_headers = {
            'head1': 'head1',
            'Authorization': f'Bearer {API_KEY}'
        }
        assert actual_headers == expected_headers

    def test_covert_record_to_myvr_object(self):
        response = {
            'key': 'key1',
            'name': 'name1'
        }
        myvr_record = self.resource.convert_to_myvr_object(response)

        assert isinstance(myvr_record, MyVRObject)
        assert dict(myvr_record) == response

    def test_convert_list_to_myvr_object(self, resource_list_data):
        myvr_collection = self.resource.convert_to_myvr_object(resource_list_data)

        assert isinstance(myvr_collection, MyVRCollection)
        assert len(myvr_collection) == len(resource_list_data['results'])
        assert list(myvr_collection) == resource_list_data['results']
        assert myvr_collection.meta['limit'] == resource_list_data['limit']
        assert myvr_collection.meta['offset'] == resource_list_data['offset']
        assert myvr_collection.meta['count'] == resource_list_data['count']

    def test_create_resource_with_invalid_api_url(self):
        with pytest.raises(ResourceUrlError):
            class MyResource(APIResource):
                model_name = 'MyResource'
                resource_url = '/my-resource/'

            MyResource('api_key', 'api_url', 'v1')

    def test_create_resource_with_invalid_resource_url(self):
        with pytest.raises(ResourceUrlError):
            class MyResource(APIResource):
                model_name = 'MyResource'
                resource_url = '/my-resource'

            MyResource('api_key', 'api_url/', 'v1')


class TestCreateMixin:
    class MyResource(CreateMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_create(self, api_url, resource_data):
        resource_url = f"{api_url}{self.MyResource.resource_url}"
        with requests_mock.Mocker() as m:
            m.post(resource_url, text=json.dumps(resource_data))

            resource = self.MyResource(API_KEY, API_URL, API_VERSION)
            response = resource.create(**resource_data)

            assert isinstance(response, MyVRObject)
            assert response.key == resource_data['key']
            assert response['name'] == resource_data['name']


class TestUpdateMixin:
    class MyResource(UpdateMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_update(self, api_url, resource_data):
        resource_url = f"{api_url}{self.MyResource.resource_url}{resource_data['key']}/"
        with requests_mock.Mocker() as m:
            m.put(resource_url, text=json.dumps(resource_data))
            resource = self.MyResource(API_KEY, API_URL, API_VERSION)
            response = resource.update(**resource_data)

            assert isinstance(response, MyVRObject)
            assert response.key == resource_data['key']
            assert response['name'] == resource_data['name']


class TestDeleteMixin:
    class MyResource(DeleteMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_delete(self, api_url, resource_data):
        resource_url = f"{api_url}{self.MyResource.resource_url}{resource_data['key']}/"
        with requests_mock.Mocker() as m:
            m.delete(resource_url, text='{}')
            resource = self.MyResource(API_KEY, API_URL, API_VERSION)
            response = resource.delete(resource_data['key'])

            assert isinstance(response, MyVRObject)
            assert len(response) == 0
            assert response.key is None


class TestListMixin:
    class MyResource(ListMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_list(self, api_url, resource_list_data):
        resource_url = f"{api_url}{self.MyResource.resource_url}"
        with requests_mock.Mocker() as m:
            m.get(resource_url, text=json.dumps(resource_list_data))

            resource = self.MyResource(API_KEY, API_URL, API_VERSION)
            response = resource.list()

            assert isinstance(response, MyVRCollection)
            assert list(response) == resource_list_data['results']
