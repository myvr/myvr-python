import json

from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import MessageTemplate
from tests.utils import API_SOURCE_URL, get_common_actions, init_resource


class TestMessageTemplate:
    def test_settings(self):
        assert MessageTemplate.resource_url == '/message-templates/'
        assert MessageTemplate.model_name == 'Message Template'

    def test_base_actions(self):
        expected_actions = {RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(MessageTemplate, expected_actions)

        assert len(actual_actions) == len(expected_actions)

    def test_render(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + MessageTemplate.resource_url + resource_data['key'] + '/render/'
        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = init_resource(MessageTemplate).render(resource_data['key'])

        assert response.key == resource_data['key']
