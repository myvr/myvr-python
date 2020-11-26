import json

from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources.bookings.reservation import Reservation
from tests.utils import API_SOURCE_URL, get_resource_actions, init_resource, sort_actions


class TestReservation:
    @property
    def resource(self) -> Reservation:
        return init_resource(Reservation)

    def test_settings(self):
        assert Reservation.resource_url == '/reservations/'
        assert Reservation.model_name == 'Reservation'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, UpdateMixin, ListMixin])
        actual_actions = get_resource_actions(Reservation)

        assert actual_actions == expected_actions

    def build_url(self, key: str, path: str) -> str:
        return API_SOURCE_URL + self.resource.resource_url + key + path

    def test_update(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/')

        requests_mock.patch(resource_url, text=json.dumps(resource_data))
        response = self.resource.update(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_create_from_quote(self, requests_mock, resource_data):
        resource_url = API_SOURCE_URL + self.resource.resource_url

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.create_from_quote()
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_update_from_quote(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/')

        requests_mock.put(resource_url, text=json.dumps(resource_data))
        response = self.resource.update_from_quote(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_cancel(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/cancel/')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.cancel(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_decline(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/decline/')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.decline(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_approve(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/approve/')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.approve(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']

    def test_assign(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/assign/')

        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.assign(resource_data['key'])
        assert isinstance(response, MyVRObject)
        assert response.key == resource_data['key']
