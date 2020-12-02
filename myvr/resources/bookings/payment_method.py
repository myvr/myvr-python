from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class PaymentMethod(CreateMixin, RetrieveMixin, ListMixin):
    path = 'reservation-payment-methods'
    name = 'Reservation Payment Method'
