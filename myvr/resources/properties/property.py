from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin


class Property(CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/properties/'
    model_name = 'Property'

    def reset_rate(self, key: str, **kwargs):
        url = self.get_key_url(key) + 'rates/'
        return self.request('PUT', url, data=kwargs)
