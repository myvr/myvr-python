import json

import pytest

from myvr import MyVRAPIException
from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import RatePlan
from tests.utils import API_KEY, API_URL, API_VERSION, get_resource_actions, sort_actions


class TestRatePlanResource:
    def test_settings(self):
        assert RatePlan.resource_url == '/rate-plans/'
        assert RatePlan.model_name == 'Rate Plan'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(RatePlan)

        assert actual_actions == expected_actions


class TestResetRateMethod:
    @property
    def resource(self):
        return RatePlan(API_KEY, API_URL, API_VERSION)

    def test_invalid_body(self, requests_mock, api_url, key):
        status_code = 400
        actual_response = {'non_field_errors': ['Expected a list of items but got type "dict".']}
        resource_url = f"{api_url}{self.resource.resource_url}{key}/rates/"
        requests_mock.put(resource_url, text=json.dumps(actual_response), status_code=status_code)

        with pytest.raises(MyVRAPIException) as e:
            self.resource.request('PUT', resource_url)

        error_data = e.value.data
        assert error_data['status_code'] == status_code
        assert error_data['message'] == actual_response

    def test_correct_body(self, requests_mock, api_url, key):
        expected_response = {}
        resource_url = f"{api_url}{self.resource.resource_url}{key}/rates/"

        requests_mock.put(resource_url, text=json.dumps(expected_response))
        res = self.resource.request('PUT', resource_url)

        assert isinstance(res, MyVRObject)
        assert res.key is None
