from myvr.api.mixins import ModelViewSet


class CalendarEvent(ModelViewSet):
    resource_url = '/calendar-events/'
    model_name = 'Calendar Event'
