import json

import pytest

from myvr.api.exceptions import MyVRAPIError
from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import Property
from tests.utils import API_SOURCE_URL, MockClient
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestPropertyResource:
    def test_settings(self):
        assert Property.path == 'properties'
        assert Property.name == 'Property'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Property)

        assert actual_actions == expected_actions


class TestResetRateMethod:
    def test_invalid_body(self, requests_mock, key, myvr_client: MockClient):
        status_code = 400
        actual_response = {'non_field_errors': ['Expected a list of items but got type "dict".']}
        resource_url = f"{API_SOURCE_URL}/{myvr_client.Property.path}/{key}/rates/"
        requests_mock.put(
            resource_url,
            text=json.dumps(actual_response),
            status_code=status_code
        )

        with pytest.raises(MyVRAPIError) as e:
            myvr_client.Property.reset_rate(key)

        error_data = e.value.data
        assert error_data['status_code'] == status_code
        assert error_data['message'] == actual_response

    def test_correct_body(self, requests_mock, key, myvr_client: MockClient):
        expected_response = {}
        resource_url = f"{API_SOURCE_URL}/{myvr_client.Property.path}/{key}/rates/"

        requests_mock.put(resource_url, text=json.dumps(expected_response))
        res = myvr_client.Property.reset_rate(key)

        assert isinstance(res, MyVRObject)
        assert res.key is None
