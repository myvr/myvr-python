from functools import partialmethod

from myvr.api.mixins import ModelViewSet
from myvr.api.resource import APIResource


class Property(ModelViewSet):
    resource_url = 'properties'
    resource_name = 'Property'

    reset_rate = partialmethod(APIResource.object_action, path='rates/')
