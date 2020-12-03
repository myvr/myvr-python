from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import ContactAddress
from tests.utils import get_resource_actions, sort_actions


class TestContactAddress:
    def test_settings(self):
        assert ContactAddress.path == 'contact-addresses'
        assert ContactAddress.name == 'Contact Address'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(ContactAddress)

        assert actual_actions == expected_actions
