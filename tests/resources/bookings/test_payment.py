import json

from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import Payment
from tests.utils import API_SOURCE_URL, create_client
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestPayment:
    @property
    def client(self):
        return create_client()

    def test_settings(self):
        assert Payment.path == 'reservation-payments'
        assert Payment.name == 'Reservation Payment'

    def test_base_actions(self):
        expected_actions = sort_actions(
            [CreateMixin, RetrieveMixin, ListMixin]
        )
        actual_actions = get_resource_actions(Payment)

        assert actual_actions == expected_actions

    def build_url(self, key: str, path: str) -> str:
        return API_SOURCE_URL + f'/{self.client.Payment.path}/{key}/{path}/'

    def test_process(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], 'process')
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        response = self.client.Payment.process(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_refund(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], 'refund')
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        response = self.client.Payment.refund(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_record(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], 'record')
        requests_mock.post(resource_url, text=json.dumps(resource_data))

        response = self.client.Payment.record(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
