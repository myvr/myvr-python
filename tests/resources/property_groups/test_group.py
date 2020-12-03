from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin

from myvr.resources import Group
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestGroupResource:
    def test_settings(self):
        assert Group.path == 'property-groups'
        assert Group.name == 'Group'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        ])
        actual_actions = get_resource_actions(Group)
        assert actual_actions == expected_actions
