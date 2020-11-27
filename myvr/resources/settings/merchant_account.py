from myvr.api.mixins import RetrieveMixin, ListMixin


class MerchantAccount(RetrieveMixin, ListMixin):
    resource_url = '/merchant-accounts/'
    model_name = 'Merchant Account'
