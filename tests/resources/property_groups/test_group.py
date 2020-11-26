from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Group
from tests.utils import get_common_actions


class TestGroupResource:
    def test_settings(self):
        assert Group.resource_url == '/property-groups/'
        assert Group.model_name == 'Group'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        }
        actual_actions = get_common_actions(Group, expected_actions)

        assert len(actual_actions) == len(expected_actions)
