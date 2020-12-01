from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class CancellationReason(RetrieveMixin, ListMixin):
    resource_url = 'reservation-cancellation-reasons'
    resource_name = 'Reservation Cancellation Reason'
