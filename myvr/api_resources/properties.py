from myvr.api_resources.abstract import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class Property(CreateMixin, UpdateMixin, DeleteMixin, ListMixin):

    base_url = 'https://api.myvr.com/v1/properties/'
    model_name = 'Property'

    @classmethod
    def reset_rate(cls, key: str, api_key='', **kwargs):
        instance = cls(api_key=api_key)
        return instance.request('PUT', cls.base_url + f'{key}/rates/', data=kwargs)
