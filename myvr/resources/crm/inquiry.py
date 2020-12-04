from functools import partialmethod

from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.resource import APIResource


class Inquiry(CreateMixin, RetrieveMixin, ListMixin):
    path = 'inquiries'
    name = 'Inquiry'

    assign = partialmethod(APIResource.object_action, path='assign')
