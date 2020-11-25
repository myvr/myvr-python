from myvr.api.mixins import ModelViewSet


class Fee(ModelViewSet):
    resource_url = '/fees/'
    model_name = 'Fee'
