from myvr.api.mixins import ModelViewSet


class Room(ModelViewSet):
    resource_url = '/rooms/'
    model_name = 'Room'
