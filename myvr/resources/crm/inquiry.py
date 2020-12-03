from functools import partialmethod

from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.api.resource import APIResource


class Inquiry(CreateMixin, RetrieveMixin, ListMixin):
    path = 'inquiries'
    name = 'Inquiry'

    assign = partialmethod(APIResource.object_action, path='assign')
