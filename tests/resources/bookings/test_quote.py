import json

import requests_mock

from myvr.api.mixins import CreateMixin, RetrieveMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources.bookings.quote import Quote
from tests.conftest import API_KEY, API_URL, API_VERSION


class TestQuote:
    def test_settings(self):
        assert Quote.resource_url == '/quotes/'
        assert Quote.model_name == 'Quote'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin}
        actual_actions = set(Quote.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)

    def test_create_custom(self, api_url, resource_data):
        resource_url = f'{api_url}{Quote.resource_url}' + 'custom/'

        with requests_mock.Mocker() as m:
            m.post(resource_url, text=json.dumps(resource_data))

            resource = Quote(API_KEY, API_URL, API_VERSION)
            response = resource.create_custom()

            assert isinstance(response, MyVRObject)
            assert response.key == resource_data['key']
