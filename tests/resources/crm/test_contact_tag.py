from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import ContactTag
from tests.utils import get_resource_actions, sort_actions


class TestContactTag:
    def test_settings(self):
        assert ContactTag.path == 'contact-tags'
        assert ContactTag.name == 'Contact Tag'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin])
        actual_actions = get_resource_actions(ContactTag)

        assert actual_actions == expected_actions
