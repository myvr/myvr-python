from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin
from myvr.resources import Tag
from tests.utils import get_resource_actions, sort_actions


class TestTag:
    def test_settings(self):
        assert Tag.resource_url == '/tags/'
        assert Tag.model_name == 'Tag'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, DeleteMixin, ListMixin])
        actual_actions = get_resource_actions(Tag)

        assert actual_actions == expected_actions
