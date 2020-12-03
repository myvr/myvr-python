import json

from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import MessageTemplate
from tests.utils import API_SOURCE_URL, MockClient, get_resource_actions, sort_actions


class TestMessageTemplate:
    def test_settings(self):
        assert MessageTemplate.path == 'message-templates'
        assert MessageTemplate.name == 'Message Template'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(MessageTemplate)

        assert actual_actions == expected_actions

    def test_render(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = API_SOURCE_URL + f"/{MessageTemplate.path}/{resource_data['key']}/render/"
        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = myvr_client.MessageTemplate.render(resource_data['key'])

        assert response.key == resource_data['key']
