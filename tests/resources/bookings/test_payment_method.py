from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin

from myvr.resources.bookings.payment_method import PaymentMethod

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestPaymentMethod:
    def test_settings(self):
        assert PaymentMethod.path == 'reservation-payment-methods'
        assert PaymentMethod.name == 'Reservation Payment Method'

    def test_base_actions(self):
        expected_actions = sort_actions(
            [CreateMixin, RetrieveMixin, ListMixin]
        )
        actual_actions = get_resource_actions(PaymentMethod)

        assert actual_actions == expected_actions
