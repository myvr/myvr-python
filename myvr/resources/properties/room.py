from myvr.api.abstract import CreateMixin, UpdateMixin, DeleteMixin, ListMixin


class Room(CreateMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/rooms/'
    model_name = 'Room'
