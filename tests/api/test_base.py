import json

import pytest

from myvr.api.base import APIResource
from myvr.api.exceptions import MyVRAPIException, ResourceUrlError
from myvr.api.myvr_objects import MyVRCollection, MyVRObject
from tests.utils import API_KEY, API_URL, API_VERSION


class TestApiResource:
    class MyResource(APIResource):
        model_name = 'MyResource'
        resource_url = '/my-resource/'

    @property
    def resource(self):
        return self.MyResource(API_KEY, API_URL, API_VERSION)

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

    def test_make_bad_request(self, requests_mock, api_url):
        actual_response = {
            'key': ['Field is required']
        }
        status_code = 400
        resource_url = f"{api_url}{self.MyResource.resource_url}"

        requests_mock.post(
            resource_url,
            text=json.dumps(actual_response),
            status_code=status_code
        )
        with pytest.raises(MyVRAPIException) as e:
            self.resource.request('POST', self.resource.base_url)

        error_data = e.value.data
        assert error_data['status_code'] == status_code
        assert error_data['message'] == actual_response

    def test_string_response(self, requests_mock, api_url):
        text = 'string'
        resource_url = f"{api_url}{self.MyResource.resource_url}"

        requests_mock.get(resource_url, text=text)
        response = self.resource.request('GET', self.resource.base_url)
        assert response.response_text == text

    def test_list_response(self, requests_mock, api_url):
        resource_url = f"{api_url}{self.MyResource.resource_url}"

        requests_mock.get(resource_url, text='[]')
        response = self.resource.request('GET', self.resource.base_url)
        assert isinstance(response, list)
