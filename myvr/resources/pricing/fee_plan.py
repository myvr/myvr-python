from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class FeePlan(RetrieveMixin, ListMixin):
    path = 'fee-plans'
    name = 'Fee Plan'
