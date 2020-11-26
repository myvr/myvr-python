from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import FeePlan
from tests.utils import get_resource_actions, sort_actions


class TestFeePlanResource:
    def test_settings(self):
        assert FeePlan.resource_url == '/fee-plans/'
        assert FeePlan.model_name == 'Fee Plan'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(FeePlan)

        assert actual_actions == expected_actions
