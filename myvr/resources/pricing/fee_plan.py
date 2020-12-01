from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class FeePlan(RetrieveMixin, ListMixin):
    resource_url = 'fee-plans'
    resource_name = 'Fee Plan'
