from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin


class CalendarEvent(CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/calendar-events/'
    model_name = 'Calendar Event'
