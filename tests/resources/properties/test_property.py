import json

import pytest

from myvr import exceptions
from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import Property
from tests.utils import API_SOURCE_URL, get_resource_actions, init_resource, sort_actions


class TestPropertyResource:
    def test_settings(self):
        assert Property.resource_url == '/properties/'
        assert Property.model_name == 'Property'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Property)

        assert actual_actions == expected_actions


class TestResetRateMethod:
    @property
    def resource(self) -> Property:
        return init_resource(Property)

    def test_invalid_body(self, requests_mock, key):
        status_code = 400
        actual_response = {'non_field_errors': ['Expected a list of items but got type "dict".']}
        resource_url = f"{API_SOURCE_URL}{self.resource.resource_url}{key}/rates/"
        requests_mock.put(resource_url, text=json.dumps(actual_response), status_code=status_code)

        with pytest.raises(exceptions.MyVRAPIException) as e:
            self.resource.request('PUT', resource_url)

        error_data = e.value.data
        assert error_data['status_code'] == status_code
        assert error_data['message'] == actual_response

    def test_correct_body(self, requests_mock, key):
        expected_response = {}
        resource_url = f"{API_SOURCE_URL}{self.resource.resource_url}{key}/rates/"

        requests_mock.put(resource_url, text=json.dumps(expected_response))
        res = self.resource.request('PUT', resource_url)

        assert isinstance(res, MyVRObject)
        assert res.key is None
