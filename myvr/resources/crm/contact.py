from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin


class Contact(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    path = 'contacts'
    name = 'Contact'
