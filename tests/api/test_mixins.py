import json

from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.api.myvr_objects import MyVRCollection, MyVRObject
from tests.utils import API_KEY, API_SOURCE_URL, API_URL, API_VERSION


class TestCreateMixin:
    class MyResource(CreateMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_create(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + self.MyResource.resource_url
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        resource = self.MyResource(API_KEY, API_URL, API_VERSION)
        response = resource.create(**resource_data)

        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
        assert response['name'] == resource_data['name']


class TestRetrieveMixin:
    class MyResource(RetrieveMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_retrieve(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + self.MyResource.resource_url + resource_data['key'] + '/'

        requests_mock.get(resource_url, text=json.dumps(resource_data))
        resource = self.MyResource(API_KEY, API_URL, API_VERSION)
        res = resource.retrieve(resource_data['key'])

        assert isinstance(res, MyVRObject)
        assert res.key == resource_data['key']


class TestUpdateMixin:
    class MyResource(UpdateMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_update(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + self.MyResource.resource_url + resource_data['key'] + '/'
        requests_mock.put(resource_url, text=json.dumps(resource_data))
        resource = self.MyResource(API_KEY, API_URL, API_VERSION)
        response = resource.update(**resource_data)

        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
        assert response['name'] == resource_data['name']


class TestDeleteMixin:
    class MyResource(DeleteMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_delete(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + self.MyResource.resource_url + resource_data['key'] + '/'
        requests_mock.delete(resource_url, text='{}')
        resource = self.MyResource(API_KEY, API_URL, API_VERSION)
        response = resource.delete(resource_data['key'])

        assert isinstance(response, MyVRObject)
        assert len(response) == 0
        assert response.key is None


class TestListMixin:
    class MyResource(ListMixin):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    def test_list(self, requests_mock, resource_list_data):
        resource_url = API_SOURCE_URL + self.MyResource.resource_url
        requests_mock.get(resource_url, text=json.dumps(resource_list_data))

        resource = self.MyResource(API_KEY, API_URL, API_VERSION)
        response = resource.list()

        assert isinstance(response, MyVRCollection)
        assert list(response) == resource_list_data['results']

    def test_list_with_query(self, requests_mock):
        resource_url = f'{API_SOURCE_URL}{self.MyResource.resource_url}?a=1&b=2'
        expected_result = [
            {'key': 'key1', 'name': 'name1'},
            {'key': 'key2', 'name': 'name2'},
        ]
        requests_mock.get(resource_url, text=json.dumps(expected_result))

        resource = self.MyResource(API_KEY, API_URL, API_VERSION)
        response = resource.list(query_params={'a': 1, 'b': 2})

        assert isinstance(response, MyVRCollection)
        assert len(response) == len(expected_result)
