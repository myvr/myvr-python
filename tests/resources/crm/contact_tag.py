from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import ContactTag
from tests.utils import get_common_actions


class TestContactTag:
    def test_settings(self):
        assert ContactTag.resource_url == '/contact-tags/'
        assert ContactTag.model_name == 'Contact Tag'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin}
        actual_actions = get_common_actions(ContactTag, expected_actions)

        assert len(actual_actions) == len(expected_actions)
