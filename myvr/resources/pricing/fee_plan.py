from myvr.api.mixins import ListMixin, RetrieveMixin


class FeePlan(RetrieveMixin, ListMixin):
    resource_url = '/fee-plans/'
    model_name = 'Fee Plan'
