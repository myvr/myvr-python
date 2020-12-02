from typing import ClassVar

from myvr.api.exceptions import ResourceUrlError
from myvr.api.myvr_objects import MyVRObject


class APIResource:
    """
    ApiResource abstract class that performs API calls and
    response processing.
    base_url: str, API-url to perform requests should be
    specified in general class not the abstract.
    model_name: str, The name of the model should be
    specified in general class not the abstract.
    """

    resource_url: ClassVar[str]
    resource_name: ClassVar[str]

    def __init__(self, client):
        """
        :param client: MyVRClient
        """

        if '/' in self.resource_url:
            raise ResourceUrlError()

        self._client = client

    @property
    def base_url(self) -> str:
        return f"{self._client.base_url}/{self.resource_url}/"

    def get_key_url(self, key: str) -> str:
        return f"{self.base_url}{key}/"

    def action(self, path: str, **data) -> MyVRObject:
        """
        Performs extra action
        :param path: action path
        :param data: dict with parameters
        :return: MyVRObject
        """

        url = self.base_url + path
        return self._client.request(
            'POST',
            url,
            self.resource_name,
            data=data
        )

    def object_action(
            self,
            key: str,
            path: str,
            method: str = 'POST',
            **data
    ) -> MyVRObject:
        """
        Performs object extra action
        :param key: Object's key
        :param path: action path
        :param data: dict with parameters
        :param method: HTTP method of the action
        :return: MyVRObject
        """

        url = self.get_key_url(key) + path
        return self._client.request(
            method,
            url,
            self.resource_name,
            data=data
        )
