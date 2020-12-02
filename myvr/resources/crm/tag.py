from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin


class Tag(CreateMixin, RetrieveMixin, DeleteMixin, ListMixin):
    resource_url = '/tags/'
    model_name = 'Tag'
