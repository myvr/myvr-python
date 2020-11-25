from myvr.api.mixins import ListMixin, RetrieveMixin


class Refund(RetrieveMixin, ListMixin):
    resource_url = '/reservation-refunds/'
    model_name = 'Reservation Refund'
