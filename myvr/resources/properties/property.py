from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import ModelViewSet


class Property(ModelViewSet):
    resource_url = '/properties/'
    model_name = 'Property'

    reset_rate = partialmethod(APIResource.object_action, path='rates/')
