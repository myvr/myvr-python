from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import ChannelListing
from tests.utils import get_common_actions


class TestChannelListing:
    def test_settings(self):
        assert ChannelListing.resource_url == '/channel-listings/'
        assert ChannelListing.model_name == 'Channel Listing'

    def test_base_actions(self):
        expected_actions = {
            RetrieveMixin, ListMixin
        }
        actual_actions = get_common_actions(ChannelListing, expected_actions)

        assert len(actual_actions) == len(expected_actions)
