from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class MerchantAccount(RetrieveMixin, ListMixin):
    path = 'merchant-accounts'
    name = 'Merchant Account'
