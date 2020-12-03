import json
from urllib import parse

import pytest

from myvr.api.exceptions import MyVRAPIError
from myvr.api.myvr_objects import MyVRCollection, MyVRObject
from tests.utils import API_KEY, API_SOURCE_URL, create_client


class TestMyVRClient:
    resource_url = 'test-url/'
    resource_name = 'test'

    @property
    def client(self):
        return create_client()

    def test_get_headers(self):
        headers = {}
        actual_headers = self.client.get_headers(headers)
        expected_headers = {
            'Authorization': f'Bearer {API_KEY}'
        }
        assert actual_headers == expected_headers

    def test_get_headers_with_other_headers(self):
        headers = {
            'head1': 'head1',
        }
        actual_headers = self.client.get_headers(headers)
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
        myvr_record = self.client.convert_to_myvr_object(response, self.resource_name)

        assert isinstance(myvr_record, MyVRObject)
        assert dict(myvr_record) == response

    def test_convert_list_to_myvr_object(self, resource_list_data):
        myvr_collection = self.client.convert_to_myvr_object(
            resource_list_data, self.resource_name
        )

        assert isinstance(myvr_collection, MyVRCollection)
        assert len(myvr_collection) == len(resource_list_data['results'])
        assert list(myvr_collection) == resource_list_data['results']
        assert myvr_collection.meta['limit'] == resource_list_data['limit']
        assert myvr_collection.meta['offset'] == resource_list_data['offset']
        assert myvr_collection.meta['count'] == resource_list_data['count']

    def test_make_bad_request(self, requests_mock):
        actual_response = {
            'key': ['Field is required']
        }
        status_code = 400
        resource_url = API_SOURCE_URL + 'test-url/'

        requests_mock.post(
            resource_url,
            text=json.dumps(actual_response),
            status_code=status_code
        )
        with pytest.raises(MyVRAPIError) as e:
            self.client.request(
                'POST',
                resource_url,
                self.resource_name
            )

        error_data = e.value.data
        assert error_data['status_code'] == status_code
        assert error_data['message'] == actual_response

    def test_string_response(self, requests_mock):
        text = 'string'
        resource_url = API_SOURCE_URL + self.resource_url
        requests_mock.get(resource_url, text=text)
        response = self.client.request(
            'GET',
            resource_url,
            self.resource_name
        )
        assert response.response_text == text

    def test_list_response(self, requests_mock):
        resource_url = API_SOURCE_URL + self.resource_url
        requests_mock.get(resource_url, text='[]')
        response = self.client.request(
            'GET',
            resource_url,
            self.resource_name
        )
        assert isinstance(response, list)

    def test_request_with_query_string(self, requests_mock):
            limit, offset = 0, 0
            query_params = {
                'a': 1,
                'b': 2,
                'limit': limit,
                'offset': offset
            }
            query = parse.urlencode(query_params)
            resource_url = f'{API_SOURCE_URL}?{query}'

            requests_mock.get(resource_url, text='{}')

            response = self.client.request(
                method='GET',
                url=API_SOURCE_URL,
                model_name=self.resource_name,
                query_params=query_params,
            )
            assert response == {}
