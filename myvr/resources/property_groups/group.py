from myvr.api.mixins import ModelViewSet


class Group(ModelViewSet):
    resource_url = '/property-groups/'
    model_name = 'Group'
