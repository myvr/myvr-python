from myvr.api.mixins import ModelViewSet


class Amenity(ModelViewSet):
    resource_url = 'property-amenities'
    resource_name = 'Amenity'
