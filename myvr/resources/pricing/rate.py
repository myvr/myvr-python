from myvr.api.mixins import ModelViewSet


class Rate(ModelViewSet):
    resource_url = 'rates'
    resource_name = 'Rate'
