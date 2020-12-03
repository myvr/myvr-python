from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import User
from tests.utils import get_resource_actions, sort_actions


class TestUser:
    def test_settings(self):
        assert User.path == 'users'
        assert User.name == 'User'

    def test_base_actions(self):
        expected_actions = sort_actions([ListMixin, RetrieveMixin])
        actual_actions = get_resource_actions(User)

        assert actual_actions == expected_actions
