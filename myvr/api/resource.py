from typing import ClassVar

from myvr.api.exceptions import ResourceUrlError
from myvr.api.myvr_objects import MyVRObject


class APIResource:
    """
    ApiResource abstract class that performs API calls and
    response processing.
    base_url: str, API-url to perform requests should be
    specified in general class not the abstract.
    name: str, The name of the model should be
    specified in general class not the abstract.
    """

    path: ClassVar[str]
    name: ClassVar[str]

    def __init__(self, client):
        """
        :param client: MyVRClient
        """

        if '/' in self.path:
            raise ResourceUrlError()

        self._client = client

    def action(self, path: str, **data) -> MyVRObject:
        """
        Performs extra action
        :param path: action path
        :param data: dict with parameters
        :return: MyVRObject
        """

        url = self.add_path(self.base_url, path)
        return self._client.request(
            'POST',
            url,
            self.name,
            data=data
        )

    def object_action(
            self,
            object_key: str,
            path: str,
            method: str = 'POST',
            **data
    ) -> MyVRObject:
        """
        Performs object extra action
        :param object_key: Object's key
        :param path: action path
        :param data: dict with parameters
        :param method: HTTP method of the action
        :return: MyVRObject
        """

        url = self.add_path(self.base_url, object_key, path)
        return self._client.request(
            method,
            url,
            self.name,
            data=data
        )

    @property
    def base_url(self) -> str:
        return self.add_path(self._client.base_url, self.path)

    @classmethod
    def add_path(cls, url: str, *paths) -> str:
        delimiter = '/'
        if not url.endswith(delimiter):
            url += delimiter
        return url + delimiter.join(paths) + delimiter
