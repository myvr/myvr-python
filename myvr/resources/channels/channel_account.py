from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class ChannelAccount(RetrieveMixin, ListMixin):
    path = 'channel-accounts'
    name = 'Channel Account'
