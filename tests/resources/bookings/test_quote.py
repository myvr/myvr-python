import json

from myvr.api.mixins import CreateMixin, RetrieveMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources.bookings.quote import Quote
from tests.utils import get_resource_actions, init_resource, sort_actions


class TestQuote:
    def test_settings(self):
        assert Quote.resource_url == '/quotes/'
        assert Quote.model_name == 'Quote'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin])
        actual_actions = get_resource_actions(Quote)

        assert actual_actions == expected_actions

    def test_create_custom(self, requests_mock, api_url, resource_data):
        resource_url = f'{api_url}{Quote.resource_url}' + 'custom/'

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = init_resource(Quote).create_custom()

        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
