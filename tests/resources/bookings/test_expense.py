from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import Expense
from tests.utils import get_common_actions


class TestExpense:
    def test_settings(self):
        assert Expense.resource_url == '/reservation-expenses/'
        assert Expense.model_name == 'Reservation Expense'

    def test_base_actions(self):
        expected_actions = {RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(Expense, expected_actions)

        assert len(actual_actions) == len(expected_actions)
