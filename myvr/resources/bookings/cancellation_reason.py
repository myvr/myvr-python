from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class CancellationReason(RetrieveMixin, ListMixin):
    path = 'reservation-cancellation-reasons'
    name = 'Reservation Cancellation Reason'
