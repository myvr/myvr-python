from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class Refund(RetrieveMixin, ListMixin):
    resource_url = 'reservation-refunds'
    resource_name = 'Reservation Refund'
