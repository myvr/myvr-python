import json

from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources.bookings.reservation import Reservation
from tests.utils import API_SOURCE_URL, MockClient
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestReservation:
    def test_settings(self):
        assert Reservation.path == 'reservations'
        assert Reservation.name == 'Reservation'

    def test_base_actions(self):
        expected_actions = sort_actions(
            [CreateMixin, RetrieveMixin, UpdateMixin, ListMixin]
        )
        actual_actions = get_resource_actions(Reservation)

        assert actual_actions == expected_actions

    @classmethod
    def build_url(cls, client: MockClient, key: str, path: str = '') -> str:
        url = API_SOURCE_URL + f'/{client.Reservation.path}/{key}/{path}'
        if path:
            url += '/'
        return url

    def test_update(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = self.build_url(myvr_client, resource_data['key'])

        requests_mock.patch(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Reservation.update(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_create_from_quote(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = API_SOURCE_URL + f'/{myvr_client.Reservation.path}/'

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Reservation.create_from_quote()
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_update_from_quote(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = self.build_url(myvr_client, resource_data['key'])

        requests_mock.put(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Reservation.update_from_quote(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_cancel(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = self.build_url(myvr_client, resource_data['key'], 'cancel')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Reservation.cancel(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_decline(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = self.build_url(myvr_client, resource_data['key'], 'decline')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Reservation.decline(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_approve(self, requests_mock, resource_data, myvr_client: MockClient):
        resource_url = self.build_url(myvr_client, resource_data['key'], 'approve')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Reservation.approve(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_assign(self, requests_mock, resource_data,  myvr_client: MockClient):
        resource_url = self.build_url(myvr_client, resource_data['key'], 'assign')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = myvr_client.Reservation.assign(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
