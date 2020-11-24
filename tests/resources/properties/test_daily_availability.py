from myvr.api.mixins import ListMixin
from myvr.resources import DailyAvailability


class TestDailyAvailability:
    def test_settings(self):
        assert DailyAvailability.resource_url == '/availability/'
        assert DailyAvailability.model_name == 'Daily Availability'

    def test_base_actions(self):
        expected_actions = {ListMixin}
        actual_actions = set(DailyAvailability.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)