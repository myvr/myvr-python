import json
from typing import ClassVar, Union

import requests

from myvr.api.exceptions import MyVRAPIException, ResourceUrlError
from myvr.api.myvr_objects import MyVRCollection, MyVRObject


class BaseAPI:
    def __init__(
            self,
            api_key: str,
            api_url: str,
            version: str
    ):
        self._api_key = api_key
        self._api_url = api_url
        self._version = version

    @property
    def api_url(self) -> str:
        return self._api_url

    @property
    def version(self) -> str:
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
    def base_url(self) -> str:
        return f"{self.api_url}{self.version}{self.resource_url}"

    @property
    def auth_header(self) -> dict:
        return {'Authorization': f'Bearer {self._api_key}'}

    def get_key_url(self, key: str) -> str:
        return f"{self.base_url}{key}/"

    def get_headers(self, headers: dict) -> dict:
        if 'Authorization' not in headers:
            headers.update(self.auth_header)

        return headers

    @staticmethod
    def _verify_response(response: requests.Response) -> dict:
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
            raise MyVRAPIException(
                data={
                    'error': response.reason,
                    'method': response.request.method,
                    'status_code': response.status_code,
                    'message': response_data,
                })

        if isinstance(response_data, str):
            return {'response_text': response_data}

        return response_data

    def request(
            self,
            method: str,
            url: str,
            headers: dict = None,
            data: dict = None
    ) -> Union[MyVRObject, MyVRCollection]:
        """
        Performs request to the API.
        :param method: str, HTTP method name in uppercase
        :param url: str, The url where to send request
        :param headers: dict, Dictionary with headers, default None
        :param data: dict, Request's body, default None
        :return: MyVRObject with the fields of the model or error information
        """

        headers = self.get_headers(headers if headers else {})
        response = requests.request(method, url, headers=headers, json=data)
        data = self._verify_response(response)
        return self.convert_to_myvr_object(data)

    def convert_to_myvr_object(self, response_data: dict) -> Union[MyVRObject, MyVRCollection]:
        if isinstance(response_data, list) or 'results' in response_data:
            object_cls = MyVRCollection
        else:
            object_cls = MyVRObject

        return object_cls(response_data, self.model_name)

    def object_action(self, object_key: str, path: str, method: str = 'POST', **data) -> MyVRObject:
        """
        Performs object extra action
        :param object_key: Object's key
        :param path: action path
        :param data: dict with parameters
        :param method: HTTP method of the action
        :return: MyVRObject
        """

        url = self.get_key_url(object_key) + path
        return self.request(method, url, data=data)

    def action(self, path: str, **data) -> MyVRObject:
        """
        Performs extra action
        :param path: action path
        :param data: dict with parameters
        :return: MyVRObject
        """

        url = self.base_url + path
        return self.request('POST', url, data=data)
