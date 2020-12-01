from myvr.api.mixins import ModelViewSet


class CalendarEvent(ModelViewSet):
    resource_url = 'calendar-events'
    resource_name = 'Calendar Event'
