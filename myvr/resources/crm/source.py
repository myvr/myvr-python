from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin


class Source(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    resource_url = '/sources/'
    model_name = 'Source'
