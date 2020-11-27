import json

from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources import Inquiry
from tests.utils import API_SOURCE_URL, get_resource_actions, init_resource, sort_actions


class TestInquiry:
    def test_settings(self):
        assert Inquiry.resource_url == '/inquiries/'
        assert Inquiry.model_name == 'Inquiry'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(Inquiry)

        assert actual_actions == expected_actions

    def test_assign(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + Inquiry.resource_url + resource_data['key'] + '/assign/'

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = init_resource(Inquiry).assign(resource_data['key'])
        assert response.key == resource_data['key']
