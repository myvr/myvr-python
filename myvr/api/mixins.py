from urllib import parse

from myvr.api.base import APIResource
from myvr.api.myvr_objects import MyVRCollection, MyVRObject


class CreateMixin(APIResource):
    def create(self, **data) -> MyVRObject:
        """
        Base method to perform POST request
        :param data: dict, Request's body, default None
        :return: Created MyVRObject instance or error information
        """

        return self.request('POST', self.base_url, data=data)


class RetrieveMixin(APIResource):
    def retrieve(self, key: str, **data) -> MyVRObject:
        """
        Base method to perform GET request per one object
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        return self.request('GET', self.get_key_url(key), data=data)


class UpdateMixin(APIResource):
    def update(self, key: str, **data) -> MyVRObject:
        """
        Base method to perform PUT request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        return self.request('PUT', self.get_key_url(key), data=data)


class DeleteMixin(APIResource):
    def delete(self, key: str, **data) -> MyVRObject:
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: Empty MyVRObject instance or error information
        """

        return self.request('DELETE', self.get_key_url(key), data=data)


class ListMixin(APIResource):
    def list(
            self,
            limit: int = 0,
            offset: int = 0,
            query_params: dict = None,
            data: dict = None
    ) -> MyVRCollection:
        """
        Base method to perform GET request for many data points
        :param limit: int, Pagination parameter. The limit of the query, default 0
        :param offset: int, Pagination parameter. The offset of the query, default 0
        :param query_params: dict, params for query string
        :param data: dict, Request's body, default None
        :return: List of MyVRObject instances or error information.
        """

        if not data:
            data = {}

        if not query_params:
            query_params = {}

        if limit not in data:
            data['limit'] = limit

        if offset not in data:
            data['offset'] = offset

        query = parse.urlencode(query_params)
        url = f'{self.base_url}?{query}'

        return self.request('GET', url, data=data)


class ModelViewSet(CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin):
    """
        Generic with implementation of all base actions:
        - create
        - read
        - update
        - delete
        - list
    """
    pass
