from myvr.api.mixins import ListMixin
from myvr.resources import DailyAvailability
from tests.utils import get_common_actions


class TestDailyAvailability:
    def test_settings(self):
        assert DailyAvailability.resource_url == '/availability/'
        assert DailyAvailability.model_name == 'Daily Availability'

    def test_base_actions(self):
        expected_actions = {ListMixin}
        actual_actions = get_common_actions(DailyAvailability, expected_actions)

        assert len(actual_actions) == len(expected_actions)