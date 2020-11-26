import json

from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources import Inquiry
from tests.utils import API_SOURCE_URL, get_common_actions, init_resource


class TestInquiry:
    def test_settings(self):
        assert Inquiry.resource_url == '/inquiries/'
        assert Inquiry.model_name == 'Inquiry'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(Inquiry, expected_actions)

        assert len(actual_actions) == len(expected_actions)

    def test_assign(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + Inquiry.resource_url + resource_data['key'] + '/assign/'

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = init_resource(Inquiry).assign(resource_data['key'])
        assert response.key == resource_data['key']
