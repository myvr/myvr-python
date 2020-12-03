from myvr.api.mixins import ModelViewSet


class Amenity(ModelViewSet):
    path = 'property-amenities'
    name = 'Amenity'
