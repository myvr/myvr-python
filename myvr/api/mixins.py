from myvr.api.myvr_objects import MyVRCollection
from myvr.api.myvr_objects import MyVRObject
from myvr.api.resource import APIResource


class CreateMixin(APIResource):
    def create(self, **data) -> MyVRObject:
        """
        Base method to perform POST request
        :param data: dict, Request's body, default None
        :return: Created MyVRObject instance or error information
        """

        return self._client.request(
            'POST',
            self.base_url,
            self.name,
            data=data
        )


class RetrieveMixin(APIResource):
    def retrieve(self, key: str, **data) -> MyVRObject:
        """
        Base method to perform GET request per one object
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        url = self.add_path(self.base_url, key)
        return self._client.request(
            'GET',
            url,
            self.name,
            data=data
        )


class UpdateMixin(APIResource):
    def update(self, key: str, **data) -> MyVRObject:
        """
        Base method to perform PUT request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        url = self.add_path(self.base_url, key)
        return self._client.request(
            'PUT',
            url,
            self.name,
            data=data
        )


class DeleteMixin(APIResource):
    def delete(self, key: str, **data) -> MyVRObject:
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param data: dict, Request's body, default None
        :return: Empty MyVRObject instance or error information
        """

        url = self.add_path(self.base_url, key)
        return self._client.request(
            'DELETE',
            url,
            self.name,
            data=data
        )


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
        :param limit: int, Pagination parameter.
                The limit of the query, default 0
        :param offset: int, Pagination parameter.
                The offset of the query, default 0
        :param query_params: dict, params for query string
        :param data: dict, Request's body, default None
        :return: List of MyVRObject instances or error information.
        """

        if not data:
            data = {}

        if not query_params:
            query_params = {}

        if limit not in query_params:
            query_params['limit'] = limit

        if offset not in query_params:
            query_params['offset'] = offset

        return self._client.request(
            'GET',
            self.base_url,
            self.name,
            data=data,
            query_params=query_params,
        )


class ModelViewSet(
    CreateMixin,
    RetrieveMixin,
    UpdateMixin,
    DeleteMixin,
    ListMixin
):
    """
        Generic with implementation of all base actions:
        - create
        - read
        - update
        - delete
        - list
    """
    pass
