from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin

from myvr.resources import FeePlan

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestFeePlanResource:
    def test_settings(self):
        assert FeePlan.path == 'fee-plans'
        assert FeePlan.name == 'Fee Plan'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(FeePlan)

        assert actual_actions == expected_actions
