from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import CreateMixin, RetrieveMixin


class Quote(CreateMixin, RetrieveMixin):
    resource_url = '/quotes/'
    model_name = 'Quote'

    create_custom = partialmethod(APIResource.action, path='custom/')
