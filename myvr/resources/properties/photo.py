from myvr.api.mixins import ModelViewSet


class Photo(ModelViewSet):
    resource_url = '/photos/'
    model_name = 'Photo'
