from functools import partialmethod

from myvr.api.mixins import RetrieveMixin, ListMixin, APIResource


class RatePlan(RetrieveMixin, ListMixin):
    resource_url = '/rate-plans/'
    model_name = 'Rate Plan'

    reset_rate = partialmethod(APIResource.object_action, path='rates/', method='PUT')
