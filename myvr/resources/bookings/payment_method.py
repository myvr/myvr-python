from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin


class PaymentMethod(CreateMixin, RetrieveMixin, ListMixin):
    resource_url = '/reservation-payment-methods/'
    model_name = 'Reservation Payment Method'
