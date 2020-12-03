from myvr.api.mixins import ModelViewSet


class CalendarEvent(ModelViewSet):
    path = 'calendar-events'
    name = 'Calendar Event'
