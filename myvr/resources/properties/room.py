from myvr.api.mixins import ModelViewSet


class Room(ModelViewSet):
    resource_url = 'rooms'
    resource_name = 'Room'
