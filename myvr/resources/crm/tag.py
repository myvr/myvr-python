from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class Tag(CreateMixin, RetrieveMixin, DeleteMixin, ListMixin):
    path = 'tags'
    name = 'Tag'
