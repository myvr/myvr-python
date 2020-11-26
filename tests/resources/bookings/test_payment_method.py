from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources.bookings.payment_method import PaymentMethod
from tests.utils import get_common_actions


class TestPaymentMethod:
    def test_settings(self):
        assert PaymentMethod.resource_url == '/reservation-payment-methods/'
        assert PaymentMethod.model_name == 'Reservation Payment Method'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(PaymentMethod, expected_actions)

        assert len(actual_actions) == len(expected_actions)
