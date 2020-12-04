from myvr.api.mixins import RetrieveMixin


class Account(RetrieveMixin):
    path = 'accounts'
    name = 'Account'
