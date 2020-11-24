from myvr.api.abstract import CreateMixin, DeleteMixin, ListMixin, UpdateMixin
from myvr.resources.properties.calendar_event import CalendarEvent


class TestCalendarEvent:
    def test_settings(self):
        assert CalendarEvent.resource_url == '/calendar-events/'
        assert CalendarEvent.model_name == 'Calendar Event'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(CalendarEvent.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
