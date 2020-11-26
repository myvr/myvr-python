from myvr.api.mixins import RetrieveMixin, ListMixin


class ChannelListing(RetrieveMixin, ListMixin):
    resource_url = '/channel-listings/'
    model_name = 'Channel Listing'
