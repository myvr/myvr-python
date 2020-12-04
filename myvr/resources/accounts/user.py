from myvr.api.mixins import ListMixin, RetrieveMixin


class User(RetrieveMixin, ListMixin):
    path = 'users'
    name = 'User'
