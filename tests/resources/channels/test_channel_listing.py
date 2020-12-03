from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin

from myvr.resources import ChannelListing

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestChannelListing:
    def test_settings(self):
        assert ChannelListing.path == 'channel-listings'
        assert ChannelListing.name == 'Channel Listing'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(ChannelListing)
        assert actual_actions == expected_actions
