import json

from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin
from myvr.api.myvr_objects import MyVRCollection
from myvr.api.myvr_objects import MyVRObject
from tests.utils import API_SOURCE_URL


class TestCreateMixin:
    class MyResource(CreateMixin):
        name = 'MyResource'
        path = 'my-resource'

    def test_create(self, requests_mock, resource_data, myvr_client):
        resource_url = API_SOURCE_URL + f'/{self.MyResource.path}/'
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        resource = self.MyResource(myvr_client)
        response = resource.create(**resource_data)

        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
        assert response['name'] == resource_data['name']


class TestRetrieveMixin:
    class MyResource(RetrieveMixin):
        name = 'MyResource'
        path = 'my-resource'

    def test_retrieve(self, requests_mock, resource_data, myvr_client):
        resource_url = API_SOURCE_URL + f'/{self.MyResource.path}/' + resource_data['key'] + '/'

        requests_mock.get(resource_url, text=json.dumps(resource_data))
        resource = self.MyResource(myvr_client)
        res = resource.retrieve(resource_data['key'])

        assert isinstance(res, MyVRObject)
        assert res.key == resource_data['key']


class TestUpdateMixin:
    class MyResource(UpdateMixin):
        name = 'MyResource'
        path = 'my-resource'

    def test_update(self, requests_mock, resource_data, myvr_client):
        resource_url = f'{API_SOURCE_URL}/{self.MyResource.path}/'
        resource_url += f'{resource_data["key"]}/'
        requests_mock.put(resource_url, text=json.dumps(resource_data))
        resource = self.MyResource(myvr_client)
        response = resource.update(**resource_data)

        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
        assert response['name'] == resource_data['name']


class TestDeleteMixin:
    class MyResource(DeleteMixin):
        name = 'MyResource'
        path = 'my-resource'

    def test_delete(self, requests_mock, resource_data, myvr_client):
        resource_url = f'{API_SOURCE_URL}/{self.MyResource.path}/'
        resource_url += f'{resource_data["key"]}/'
        requests_mock.delete(resource_url, text='{}')
        resource = self.MyResource(myvr_client)
        response = resource.delete(resource_data['key'])

        assert isinstance(response, MyVRObject)
        assert len(response) == 0
        assert response.key is None


class TestListMixin:
    class MyResource(ListMixin):
        name = 'MyResource'
        path = 'my-resource'

    def test_list(self, requests_mock, resource_list_data, myvr_client):
        resource_url = API_SOURCE_URL + f'/{self.MyResource.path}/'
        requests_mock.get(resource_url, text=json.dumps(resource_list_data))

        resource = self.MyResource(myvr_client)
        response = resource.list()

        assert isinstance(response, MyVRCollection)
        assert list(response) == resource_list_data['results']
