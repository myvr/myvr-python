import json

from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources import Inquiry
from tests.utils import API_SOURCE_URL, MockClient, get_resource_actions, sort_actions


class TestInquiry:
    def test_settings(self):
        assert Inquiry.path == 'inquiries'
        assert Inquiry.name == 'Inquiry'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(Inquiry)

        assert actual_actions == expected_actions

    def test_assign(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = API_SOURCE_URL + f"/{Inquiry.path}/{resource_data['key']}/assign/"
        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Inquiry.assign(resource_data['key'])
        assert response.key == resource_data['key']
