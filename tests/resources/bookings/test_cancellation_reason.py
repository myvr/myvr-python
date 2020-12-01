from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin

from myvr.resources import CancellationReason

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestCancellationReason:
    def test_settings(self):
        resource_url = 'reservation-cancellation-reasons'
        resource_name = 'Reservation Cancellation Reason'
        assert CancellationReason.resource_url == resource_url
        assert CancellationReason.resource_name == resource_name

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(CancellationReason)

        assert actual_actions == expected_actions
