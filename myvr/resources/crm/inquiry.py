from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin


class Inquiry(CreateMixin, RetrieveMixin, ListMixin):
    resource_url = '/inquiries/'
    model_name = 'Inquiry'

    assign = partialmethod(APIResource.object_action, path='assign/')
