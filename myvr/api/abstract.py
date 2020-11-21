from myvr.api.myvr_objects import MyVRCollection, MyVRObject
from myvr.api.constants import CODE_TO_MSG
from myvr.api.exceptions import MyVRException

import requests
import json


class ApiResource:
    """
    ApiResource abstract class that performs API calls and response processing.
    base_url: str, API-url to perform requests should be specified in general class not the abstract.
    model_name: str, The name of the model should be specified in general class not the abstract.
    """

    resource_url, model_name = '', ''

    def __init__(self, api_key: str = '', api_url: str = '', version: str = 'v1'):
        """
        :param api_key: str, API key from MyVR.com
        :param api_url: str, API url to make requests
        :param version: str, API version, default v1
        """

        self._api_key = api_key
        self._version = version
        self._api_url = api_url

        if not self._api_key:
            raise MyVRException('Field: api_key should be specified')

        if not self._api_url:
            raise MyVRException('You should specify a base url for APIResource')

    @property
    def base_url(self):
        return f"{self._api_url}{self._version}{self.resource_url}"

    @property
    def auth_header(self):
        """Returns auth header"""
        return {'Authorization': f'Bearer {self._api_key}'}

    @staticmethod
    def _verify_response(response: requests.Response):
        """
        Method to check response on errors and multiple objects containing
        :param response: requests.Response, Response instance
        :return: Dictionary or List with processed values
        """

        if not response.ok:
            return {'error': CODE_TO_MSG[response.status_code], 'status_code': response.status_code}

        try:
            response = response.json()
        except json.JSONDecodeError:
            return {'response_text': response.text}

        if not isinstance(response, dict):
            raise TypeError(f'Response should be a dictionary. Given: {type(response)}')

        return response

    def request(self, method: str, url: str, headers=None, data=None):
        """
        Performs request to the API.
        :param method: str, HTTP method name in uppercase
        :param url: str, The url where to send request
        :param headers: dict, Dictionary with headers, default None
        :param data: dict, Request's body, default None
        :return: MyVRObject with the fields of the model or error information
        """

        headers = headers if headers else self.auth_header
        response = requests.request(method, url, headers=headers, data=data)
        resp = self._verify_response(response)
        return MyVRCollection(resp, self.model_name) if 'results' in resp else MyVRObject(resp, self.model_name)

    def retrieve(self, key: str, **data):
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        return self.request('GET', self.base_url + f'{key}/', data=data)


class CreateMixin(ApiResource):

    def create(self, **data):
        """
        Base method to perform POST request
        :param data: dict, Request's body, default None
        :return: Created MyVRObject instance or error information
        """

        return self.request('POST', self.base_url, data=data)


class UpdateMixin(ApiResource):

    def put(self, key, **data):
        """
        Base method to perform PUT request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        return self.request('PUT', self.base_url + f'{key}/', data=data)


class DeleteMixin(ApiResource):

    def delete(self, key, **data):
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: Empty MyVRObject instance or error information
        """

        return self.request('DELETE', self.base_url + f'{key}/', data=data)


class ListMixin(ApiResource):

    def list_objects(self, limit=0, offset=0, **data):
        """
        Base method to perform GET request for many data points
        :param limit: int, Pagination parameter. The limit of the query, default 0
        :param offset: int, Pagination parameter. The offset of the query, default 0
        :param data: dict, Request's body, default None
        :return: List of MyVRObject instances or error information
        """

        if limit not in data:
            data['limit'] = limit

        if offset not in data:
            data['offset'] = offset

        return self.request('GET', self.base_url, data=data)
