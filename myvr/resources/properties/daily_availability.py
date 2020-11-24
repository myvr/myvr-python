from myvr.api.abstract import ListMixin


class DailyAvailability(ListMixin):
    resource_url = '/availability/'
    model_name = 'Daily Availability'
