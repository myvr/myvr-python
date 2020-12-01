from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.resources import Refund
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestRefund:
    def test_settings(self):
        assert Refund.resource_url == 'reservation-refunds'
        assert Refund.resource_name == 'Reservation Refund'

    def test_base_action(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(Refund)

        assert actual_actions == expected_actions
