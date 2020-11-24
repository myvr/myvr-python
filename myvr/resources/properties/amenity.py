from myvr.api.mixins import ModelViewSet


class Amenity(ModelViewSet):
    resource_url = '/property-amenities/'
    model_name = 'Amenity'

