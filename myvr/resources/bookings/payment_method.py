from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class PaymentMethod(CreateMixin, RetrieveMixin, ListMixin):
    resource_url = 'reservation-payment-methods'
    resource_name = 'Reservation Payment Method'
