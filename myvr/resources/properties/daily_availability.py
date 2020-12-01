from myvr.api.mixins import ListMixin


class DailyAvailability(ListMixin):
    resource_url = 'availability'
    resource_name = 'Daily Availability'
