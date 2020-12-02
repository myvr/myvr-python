from functools import partialmethod

from myvr.api.mixins import CreateMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.resource import APIResource


class Quote(CreateMixin, RetrieveMixin):
    path = 'quotes'
    name = 'Quote'

    create_custom = partialmethod(APIResource.action, path='custom')
