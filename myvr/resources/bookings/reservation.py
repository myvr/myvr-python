from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin


class Reservation(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    resource_url = '/reservations/'
    model_name = 'Reservation'

    create_from_quote = partialmethod(CreateMixin.create)
    update_from_quote = partialmethod(UpdateMixin.update)
    cancel = partialmethod(APIResource.action, path='cancel/')
    decline = partialmethod(APIResource.action, path='decline/')
    approve = partialmethod(APIResource.action, path='approve/')
    assign = partialmethod(APIResource.action, path='assign/')
