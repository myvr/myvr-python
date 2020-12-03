from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Contact
from tests.utils import API_SOURCE_URL, MockClient, get_resource_actions, sort_actions


class TestContact:
    @classmethod
    def build_url(cls, client: MockClient, key: str, path: str) -> str:
        return API_SOURCE_URL + client.Contact.path + key + path

    def test_settings(self):
        assert Contact.path == 'contacts'
        assert Contact.name == 'Contact'

    def test_base_action(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, UpdateMixin, ListMixin])
        actual_actions = get_resource_actions(Contact)

        assert actual_actions == expected_actions
