import json

import requests_mock

from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.api.myvr_objects import MyVRCollection, MyVRObject
from tests.conftest import API_KEY, API_URL, API_VERSION


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


class TestRetrieveMixin:
    class MyResource(RetrieveMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_retrieve(self, api_url, resource_data):
        with requests_mock.Mocker() as m:
            resource_url = f"{api_url}{self.MyResource.resource_url}{resource_data['key']}/"

            m.get(resource_url, text=json.dumps(resource_data))
            resource = self.MyResource(API_KEY, API_URL, API_VERSION)
            res = resource.retrieve(resource_data['key'])

            assert isinstance(res, MyVRObject)
            assert res.key == resource_data['key']


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

    def test_list_with_query(self, api_url):
        resource_url = f'{api_url}{self.MyResource.resource_url}?a=1&b=2'
        expected_result = [
            {'key': 'key1', 'name': 'name1'},
            {'key': 'key2', 'name': 'name2'},
        ]
        with requests_mock.Mocker() as m:
            m.get(resource_url, text=json.dumps(expected_result))

            resource = self.MyResource(API_KEY, API_URL, API_VERSION)
            response = resource.list(query_params={'a': 1, 'b': 2})

            assert isinstance(response, MyVRCollection)
            assert len(response) == len(expected_result)
