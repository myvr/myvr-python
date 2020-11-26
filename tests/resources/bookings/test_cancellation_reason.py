from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import CancellationReason
from tests.utils import get_common_actions


class TestCancellationReason:
    def test_settings(self):
        assert CancellationReason.resource_url == '/reservation-cancellation-reasons/'
        assert CancellationReason.model_name == 'Reservation Cancellation Reason'

    def test_base_actions(self):
        expected_actions = {RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(CancellationReason, expected_actions)

        assert len(actual_actions) == len(expected_actions)
