import json

from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import Payment
from tests.utils import API_KEY, API_URL, API_VERSION, get_common_actions


class TestPayment:
    @property
    def resource(self):
        return Payment(API_KEY, API_URL, API_VERSION)

    def test_settings(self):
        assert Payment.resource_url == '/reservation-payments/'
        assert Payment.model_name == 'Reservation Payment'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(Payment, expected_actions)

        assert len(actual_actions) == len(expected_actions)

    def test_process(self, requests_mock, api_url, resource_data):
        resource_url = api_url + Payment.resource_url + resource_data['key'] + '/process/'
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        response = self.resource.process(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_refund(self, requests_mock, api_url, resource_data):
        resource_url = api_url + Payment.resource_url + resource_data['key'] + '/refund/'
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        response = self.resource.refund(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_record(self, requests_mock, api_url, resource_data):
        resource_url = api_url + Payment.resource_url + resource_data['key'] + '/record/'
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        response = self.resource.record(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
