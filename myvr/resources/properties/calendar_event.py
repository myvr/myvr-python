from myvr.api.abstract import CreateMixin, DeleteMixin, ListMixin, UpdateMixin


class CalendarEvent(CreateMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/calendar-events/'
    model_name = 'Calendar Event'
