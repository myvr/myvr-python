from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class CustomField(CreateMixin, RetrieveMixin, ListMixin):
    path = 'custom-fields'
    name = 'Custom Field'
