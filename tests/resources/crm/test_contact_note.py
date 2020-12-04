from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin
from myvr.resources import ContactNote
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestContactNone:
    def test_settings(self):
        assert ContactNote.path == 'contact-notes'
        assert ContactNote.name == 'Contact Note'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(ContactNote)

        assert actual_actions == expected_actions
