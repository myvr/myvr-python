from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class Promotion(CreateMixin, RetrieveMixin, ListMixin):
    path = 'promotions'
    name = 'Promotion'
