from myvr.api_resources.abstract import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class Property(CreateMixin, UpdateMixin, DeleteMixin, ListMixin):

    base_url = 'https://api.myvr.com/v1/properties/'

    @classmethod
    def reset_rate(cls, key, api_key=None, url=None, **kwargs):
        instance = cls(api_key=api_key, **kwargs)
        url = url if url else cls.base_url + f'{key}/rates/'
        return instance.request('PUT', url, data=kwargs)

