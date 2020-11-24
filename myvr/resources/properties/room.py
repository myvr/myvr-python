from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin


class Room(CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/rooms/'
    model_name = 'Room'
