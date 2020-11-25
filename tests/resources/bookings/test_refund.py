from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import Refund
from tests.utils import get_common_actions


class TestRefund:
    def test_settings(self):
        assert Refund.resource_url == '/reservation-refunds/'
        assert Refund.model_name == 'Reservation Refund'

    def test_base_action(self):
        expected_actions = {RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(Refund, expected_actions)

        assert len(actual_actions) == len(expected_actions)
