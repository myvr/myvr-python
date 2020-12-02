from myvr.api.mixins import ListMixin


class DailyAvailability(ListMixin):
    path = 'availability'
    name = 'Daily Availability'
