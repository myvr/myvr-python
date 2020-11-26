from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Membership
from tests.utils import get_common_actions


class TestMembershipResource:
    def test_settings(self):
        assert Membership.resource_url == '/property-memberships/'
        assert Membership.model_name == 'Membership'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        }
        actual_actions = get_common_actions(Membership, expected_actions)

        assert len(actual_actions) == len(expected_actions)
