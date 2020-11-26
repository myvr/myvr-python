from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import CancellationReason
from tests.utils import get_resource_actions, sort_actions


class TestCancellationReason:
    def test_settings(self):
        assert CancellationReason.resource_url == '/reservation-cancellation-reasons/'
        assert CancellationReason.model_name == 'Reservation Cancellation Reason'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(CancellationReason)

        assert actual_actions == expected_actions
