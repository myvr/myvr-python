from myvr.api.mixins import RetrieveMixin, ListMixin


class FeePlan(RetrieveMixin, ListMixin):
    resource_url = '/fee-plans/'
    model_name = 'Fee Plan'
