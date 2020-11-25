from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources.properties.calendar_event import CalendarEvent
from tests.utils import get_common_actions


class TestCalendarEvent:
    def test_settings(self):
        assert CalendarEvent.resource_url == '/calendar-events/'
        assert CalendarEvent.model_name == 'Calendar Event'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = get_common_actions(CalendarEvent, expected_actions)

        assert len(actual_actions) == len(expected_actions)
