from myvr.api.mixins import ListMixin
from myvr.resources import DailyAvailability
from tests.utils import get_resource_actions


class TestDailyAvailability:
    def test_settings(self):
        assert DailyAvailability.resource_url == 'availability'
        assert DailyAvailability.resource_name == 'Daily Availability'

    def test_base_actions(self):
        actual_actions = get_resource_actions(DailyAvailability)
        assert actual_actions == [ListMixin]