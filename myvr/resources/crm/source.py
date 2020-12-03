from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin


class Source(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    path = 'sources'
    name = 'Source'
