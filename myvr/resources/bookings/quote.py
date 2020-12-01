from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import CreateMixin
from myvr.api.mixins import RetrieveMixin


class Quote(CreateMixin, RetrieveMixin):
    resource_url = 'quotes'
    resource_name = 'Quote'

    create_custom = partialmethod(APIResource.action, path='custom/')
