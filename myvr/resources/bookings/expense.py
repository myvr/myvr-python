from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class Expense(RetrieveMixin, ListMixin):
    path = 'reservation-expenses'
    name = 'Reservation Expense'
