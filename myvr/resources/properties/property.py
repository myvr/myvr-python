from functools import partialmethod

from myvr.api.mixins import ModelViewSet
from myvr.api.resource import APIResource


class Property(ModelViewSet):
    path = 'properties'
    name = 'Property'

    reset_rate = partialmethod(
        APIResource.object_action,
        path='rates',
        method='PUT'
    )
