from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class ChannelListing(RetrieveMixin, ListMixin):
    path = 'channel-listings'
    name = 'Channel Listing'
