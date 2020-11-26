from myvr.api.mixins import ListMixin, RetrieveMixin


class Expense(RetrieveMixin, ListMixin):
    resource_url = '/reservation-expenses/'
    model_name = 'Reservation Expense'
