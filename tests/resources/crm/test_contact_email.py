from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin
from myvr.resources import ContactEmail
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestContactEmail:
    def test_settings(self):
        assert ContactEmail.path == 'contact-emails'
        assert ContactEmail.name == 'Contact Email'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(ContactEmail)

        assert actual_actions == expected_actions
