from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class Expense(RetrieveMixin, ListMixin):
    resource_url = 'reservation-expenses'
    resource_name = 'Reservation Expense'
