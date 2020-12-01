import json

import pytest

from myvr.api.base import APIResource
from myvr.api.exceptions import MyVRAPIError
from myvr.api.exceptions import ResourceUrlError
from myvr.api.myvr_objects import MyVRCollection
from myvr.api.myvr_objects import MyVRObject
from tests.utils import API_KEY
from tests.utils import API_SOURCE_URL
from tests.utils import API_URL
from tests.utils import API_VERSION


class TestApiResource:
    class MyResource(APIResource):
        resource_name = 'MyResource'
        resource_url = 'my-resource'

    class MyClient(MyVRClient):
        api_url = API_URL

    @property
    def client(self):
        return MyVRClient(API_KEY, API_VERSION)

    @property
    def resource(self):
        return self.MyResource(self.client)

    def test_get_headers(self):
        headers = {}
        actual_headers = self.resource._client.get_headers(headers)
        expected_headers = {
            'Authorization': f'Bearer {API_KEY}'
        }
        assert actual_headers == expected_headers

    def test_get_headers_with_other_headers(self):
        headers = {
            'head1': 'head1',
        }
        actual_headers = self.resource._client.get_headers(headers)
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
        myvr_record = self.resource._client.convert_to_myvr_object(
            response,
            self.resource.resource_name
        )

        assert isinstance(myvr_record, MyVRObject)
        assert dict(myvr_record) == response

    def test_convert_list_to_myvr_object(self, resource_list_data):
        myvr_collection = self.resource._client.convert_to_myvr_object(
            resource_list_data, self.resource.resource_name
        )

        assert isinstance(myvr_collection, MyVRCollection)
        assert len(myvr_collection) == len(resource_list_data['results'])
        assert list(myvr_collection) == resource_list_data['results']
        assert myvr_collection.meta['limit'] == resource_list_data['limit']
        assert myvr_collection.meta['offset'] == resource_list_data['offset']
        assert myvr_collection.meta['count'] == resource_list_data['count']

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

    def test_make_bad_request(self, requests_mock):
        actual_response = {
            'key': ['Field is required']
        }
        status_code = 400
        resource_url = API_SOURCE_URL + self.MyResource.resource_url

        requests_mock.post(
            resource_url,
            text=json.dumps(actual_response),
            status_code=status_code
        )
        with pytest.raises(MyVRAPIError) as e:
            self.resource._client.request(
                'POST',
                self.resource.base_url,
                self.resource.resource_name
            )

        error_data = e.value.data
        assert error_data['status_code'] == status_code
        assert error_data['message'] == actual_response

    def test_string_response(self, requests_mock):
        text = 'string'
        resource_url = API_SOURCE_URL + self.MyResource.resource_url

        requests_mock.get(resource_url, text=text)
        response = self.resource._client.request(
            'GET',
            self.resource.base_url,
            self.resource.resource_name
        )

        assert response.response_text == text

    def test_list_response(self, requests_mock):
        resource_url = API_SOURCE_URL + self.MyResource.resource_url

        requests_mock.get(resource_url, text='[]')
        response = self.resource._client.request(
            'GET',
            self.resource.base_url,
            self.resource.resource_name
        )

        assert isinstance(response, list)
