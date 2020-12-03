from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin

from myvr.resources import Membership
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestMembershipResource:
    def test_settings(self):
        assert Membership.path == 'property-memberships'
        assert Membership.name == 'Membership'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        ])
        actual_actions = get_resource_actions(Membership)
        assert actual_actions == expected_actions
