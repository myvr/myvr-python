from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class Refund(RetrieveMixin, ListMixin):
    path = 'reservation-refunds'
    name = 'Reservation Refund'
