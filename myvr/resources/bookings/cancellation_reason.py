from myvr.api.mixins import ListMixin, RetrieveMixin


class CancellationReason(RetrieveMixin, ListMixin):
    resource_url = '/reservation-cancellation-reasons/'
    model_name = 'Reservation Cancellation Reason'
