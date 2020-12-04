from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin


class Contact(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    path = 'contacts'
    name = 'Contact'
