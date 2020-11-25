from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin


class Reservation(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    resource_url = '/reservations/'
    model_name = 'Reservation'

    create_from_quote = partialmethod(CreateMixin.create)
    update_from_quote = partialmethod(UpdateMixin.update)
    cancel = partialmethod(APIResource.object_action, path='cancel/')
    decline = partialmethod(APIResource.object_action, path='decline/')
    approve = partialmethod(APIResource.object_action, path='approve/')
    assign = partialmethod(APIResource.object_action, path='assign/')
