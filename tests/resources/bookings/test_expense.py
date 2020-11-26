from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import Expense
from tests.utils import get_resource_actions, sort_actions


class TestExpense:
    def test_settings(self):
        assert Expense.resource_url == '/reservation-expenses/'
        assert Expense.model_name == 'Reservation Expense'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(Expense)

        assert actual_actions == expected_actions
