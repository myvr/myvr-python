from myvr.api.mixins import ModelViewSet


class Fee(ModelViewSet):
    resource_url = 'fees'
    resource_name = 'Fee'
