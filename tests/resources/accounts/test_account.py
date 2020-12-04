from myvr.api.mixins import RetrieveMixin
from myvr.resources import Account
from tests.utils import get_resource_actions


class TestAccount:
    def test_settings(self):
        assert Account.path == 'accounts'
        assert Account.name == 'Account'

    def test_base_actions(self):
        actual_actions = get_resource_actions(Account)
        assert actual_actions == [RetrieveMixin]
