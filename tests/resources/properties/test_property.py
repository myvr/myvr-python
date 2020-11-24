import json

import pytest
import requests_mock

from myvr import MyVRAPIException
from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import Property
from tests.conftest import API_KEY, API_URL, API_VERSION


class TestPropertyResource:
    def test_settings(self):
        assert Property.resource_url == '/properties/'
        assert Property.model_name == 'Property'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(Property.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)


class TestResetRateMethod:

    @property
    def resource(self):
        return Property(API_KEY, API_URL, API_VERSION)

    def test_invalid_body(self, key):
        status_code = 400
        actual_response = {'non_field_errors': ['Expected a list of items but got type "dict".']}
        with requests_mock.Mocker() as m:
            resource_url = f"{API_URL}{self.resource.resource_url}{key}/rates/"
            m.put(resource_url, text=json.dumps(actual_response), status_code=status_code)

            with pytest.raises(MyVRAPIException) as e:
                self.resource.request('PUT', resource_url)

            error_data = e.value.data
            assert error_data['status_code'] == status_code
            assert error_data['message'] == actual_response

    def test_correct_body(self, key, **params):
        expected_response = {}

        with requests_mock.Mocker() as m:
            resource_url = f"{API_URL}{self.resource.resource_url}{key}/rates/"

            m.put(resource_url, text=json.dumps(expected_response))
            res = self.resource.request('PUT', resource_url)

            assert isinstance(res, MyVRObject)
            assert res.key is None

