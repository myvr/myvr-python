from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import FeePlan
from tests.utils import get_common_actions


class TestFeePlanResource:
    def test_settings(self):
        assert FeePlan.resource_url == '/rate-plans/'
        assert FeePlan.model_name == 'Fee Plan'

    def test_base_actions(self):
        expected_actions = {
            RetrieveMixin, ListMixin
        }
        actual_actions = get_common_actions(FeePlan, expected_actions)

        assert len(actual_actions) == len(expected_actions)
