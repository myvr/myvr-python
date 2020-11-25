from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin


class Payment(CreateMixin, RetrieveMixin, ListMixin):
    resource_url = '/reservation-payments/'
    model_name = 'Reservation Payment'

    process = partialmethod(APIResource.object_action, path='process/')
    refund = partialmethod(APIResource.object_action, path='refund/')
    record = partialmethod(APIResource.object_action, path='record/')