from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin

from myvr.resources import ChannelAccount

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestChannelAccount:
    def test_settings(self):
        assert ChannelAccount.path == 'channel-accounts'
        assert ChannelAccount.name == 'Channel Account'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(ChannelAccount)
        assert actual_actions == expected_actions
