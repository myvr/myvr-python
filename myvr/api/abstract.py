from typing import ClassVar, Union
import requests
import json

from myvr.api.myvr_objects import MyVRCollection, MyVRObject
from myvr.api.exceptions import MyVRAPIException, ResourceUrlError


class BaseAPI:
    def __init__(self, api_key: str, api_url: str, version: str):
        self._api_key = api_key
        self._api_url = api_url
        self._version = version

    @property
    def api_url(self):
        return self._api_url

    @property
    def version(self):
        return self._version


class APIResource(BaseAPI):
    """
    ApiResource abstract class that performs API calls and response processing.
    base_url: str, API-url to perform requests should be specified in general class not the abstract.
    model_name: str, The name of the model should be specified in general class not the abstract.
    """

    resource_url: ClassVar[str]
    model_name: ClassVar[str]

    def __init__(self, api_key: str, api_url: str, version: str):
        """
        :param api_key: str, API key from MyVR.com
        :param api_url: str, API url to make requests
        :param version: str, API version, default v1
        """

        if not api_url.endswith('/'):
            raise ResourceUrlError()

        if not self.resource_url.endswith('/'):
            raise ResourceUrlError()

        self._api_key = api_key
        self._version = version
        self._api_url = api_url

        super(APIResource, self).__init__(api_key, api_url, version)


    @property
    def base_url(self):
        return f"{self.api_url}{self.version}{self.resource_url}"

    @property
    def auth_header(self):
        """Returns auth header"""
        return {'Authorization': f'Bearer {self._api_key}'}

    def get_key_url(self, key: str):
        return f"{self.base_url}{key}/"

    def get_headers(self, headers: dict):
        if 'Authorization' not in headers:
            headers.update(self.auth_header)

        return headers

    @staticmethod
    def _verify_response(response: requests.Response):
        """
        Method to check response on errors and multiple objects containing
        :param response: requests.Response, Response instance
        :return: Dictionary or List with processed values
        """

        try:
            response_data = response.json()
        except json.JSONDecodeError:
            response_data = response.text

        if not response.ok:
            raise MyVRAPIException(data={'error': response.reason, 'method': response.request.method,
                                         'status_code': response.status_code, 'message': response_data})

        if not isinstance(response_data, (dict, str)):
            raise TypeError(f'Response should be dict or str type given: {type(response_data)}')

        return {'response_text': response_data} if isinstance(response_data, str) else response_data

    def request(self, method: str, url: str, headers=None, data=None) -> Union[MyVRObject, MyVRCollection]:
        """
        Performs request to the API.
        :param method: str, HTTP method name in uppercase
        :param url: str, The url where to send request
        :param headers: dict, Dictionary with headers, default None
        :param data: dict, Request's body, default None
        :return: MyVRObject with the fields of the model or error information
        """

        headers = self.get_headers(headers if headers else {})
        response = requests.request(method, url, headers=headers, data=data)
        data = self._verify_response(response)
        return self.convert_to_myvr_object(data)

    def convert_to_myvr_object(self, response_data: dict) -> Union[MyVRObject, MyVRCollection]:
        object_cls = MyVRCollection if 'results' in response_data else MyVRObject
        return object_cls(response_data, self.model_name)

    def retrieve(self, key: str, **data):
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        return self.request('GET', self.get_key_url(key), data=data)


class CreateMixin(APIResource):

    def create(self, **data):
        """
        Base method to perform POST request
        :param data: dict, Request's body, default None
        :return: Created MyVRObject instance or error information
        """

        return self.request('POST', self.base_url, data=data)


class UpdateMixin(APIResource):

    def update(self, key: str, **data):
        """
        Base method to perform PUT request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        return self.request('PUT', self.get_key_url(key), data=data)


class DeleteMixin(APIResource):

    def delete(self, key: str, **data):
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: Empty MyVRObject instance or error information
        """

        return self.request('DELETE', self.get_key_url(key), data=data)


class ListMixin(APIResource):

    def list(self, limit: int = 0, offset: int = 0, **data):
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
