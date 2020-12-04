from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin


class Source(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    path = 'sources'
    name = 'Source'
