from functools import partialmethod

from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.resource import APIResource


class Payment(CreateMixin, RetrieveMixin, ListMixin):
    path = 'reservation-payments'
    name = 'Reservation Payment'

    process = partialmethod(APIResource.object_action, path='process')
    refund = partialmethod(APIResource.object_action, path='refund')
    record = partialmethod(APIResource.object_action, path='record')
