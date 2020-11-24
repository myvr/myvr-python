from myvr.api.mixins import CreateMixin, RetrieveMixin
from myvr.api.myvr_objects import MyVRObject


class Quote(CreateMixin, RetrieveMixin):
    resource_url = '/quotes/'
    model_name = 'Quote'

    def create_custom(self, **data) -> MyVRObject:
        url = self.base_url + 'custom/'
        return self.request('POST', url, data=data)
