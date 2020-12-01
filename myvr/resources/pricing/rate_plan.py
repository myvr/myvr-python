from functools import partialmethod

from myvr.api.mixins import APIResource
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class RatePlan(RetrieveMixin, ListMixin):
    resource_url = 'rate-plans'
    resource_name = 'Rate Plan'

    reset_rate = partialmethod(
        APIResource.object_action,
        path='rates/',
        method='PUT'
    )
