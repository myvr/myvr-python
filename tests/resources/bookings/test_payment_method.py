from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources.bookings.payment_method import PaymentMethod
from tests.utils import get_resource_actions, sort_actions


class TestPaymentMethod:
    def test_settings(self):
        assert PaymentMethod.resource_url == '/reservation-payment-methods/'
        assert PaymentMethod.model_name == 'Reservation Payment Method'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(PaymentMethod)

        assert actual_actions == expected_actions
