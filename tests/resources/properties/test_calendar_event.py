from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin

from myvr.resources.properties.calendar_event import CalendarEvent

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestCalendarEvent:
    def test_settings(self):
        assert CalendarEvent.resource_url == 'calendar-events'
        assert CalendarEvent.resource_name == 'Calendar Event'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(CalendarEvent)

        assert actual_actions == expected_actions
