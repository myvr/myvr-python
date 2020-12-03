from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin


class Tag(CreateMixin, RetrieveMixin, DeleteMixin, ListMixin):
    path = 'tags'
    name = 'Tag'
