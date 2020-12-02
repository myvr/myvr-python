from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import ContactNote
from tests.utils import get_resource_actions, sort_actions


class TestContactNone:
    def test_settings(self):
        assert ContactNote.resource_url == '/contact-notes/'
        assert ContactNote.model_name == 'Contact Note'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(ContactNote)

        assert actual_actions == expected_actions
