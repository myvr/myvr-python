from myvr.api.abstract import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class Property(CreateMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/properties/'
    model_name = 'Property'

    def reset_rate(self, key: str, **kwargs):
        url = self.get_key_url(key) + 'rates/'
        return self.request('PUT', url, data=kwargs)
