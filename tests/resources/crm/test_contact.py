import json

from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Contact
from tests.utils import API_SOURCE_URL, get_resource_actions, init_resource, sort_actions


class TestContact:
    @property
    def resource(self) -> Contact:
        return init_resource(Contact)

    def build_url(self, key: str, path: str) -> str:
        return API_SOURCE_URL + self.resource.resource_url + key + path

    def test_settings(self):
        assert Contact.resource_url == '/contacts/'
        assert Contact.model_name == 'Contact'

    def test_base_action(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, UpdateMixin, ListMixin])
        actual_actions = get_resource_actions(Contact)

        assert actual_actions == expected_actions

    def test_delete_note(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/delete-note/')
        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.delete_note(resource_data['key'])

        assert response.key == resource_data['key']

    def test_delete_phone(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/delete-phone/')
        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.delete_phone(resource_data['key'])

        assert response.key == resource_data['key']

    def test_delete_tag(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/delete-tag/')
        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.delete_tag(resource_data['key'])

        assert response.key == resource_data['key']

    def test_delete_email(self, requests_mock, resource_data):
        resource_url = self.build_url(resource_data['key'], '/delete-email/')
        requests_mock.post(resource_url, text=json.dumps(resource_data))
        response = self.resource.delete_email(resource_data['key'])

        assert response.key == resource_data['key']
