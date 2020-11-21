from myvr.api.abstract import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class Property(CreateMixin, UpdateMixin, DeleteMixin, ListMixin):

    resource_url = '/properties/'
    model_name = 'Property'

    def reset_rate(self, key: str, **kwargs):
        return self.request('PUT', self.base_url + f'{key}/rates/', data=kwargs)
