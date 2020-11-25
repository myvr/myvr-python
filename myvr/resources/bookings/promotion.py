from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin


class Promotion(CreateMixin, RetrieveMixin, ListMixin):
    resource_url = '/promotions/'
    model_name = 'Promotion'
