from myvr.api.mixins import ListMixin
from myvr.resources import DailyAvailability
from tests.utils import get_resource_actions


class TestDailyAvailability:
    def test_settings(self):
        assert DailyAvailability.path == 'availability'
        assert DailyAvailability.name == 'Daily Availability'

    def test_base_actions(self):
        actual_actions = get_resource_actions(DailyAvailability)
        assert actual_actions == [ListMixin]
