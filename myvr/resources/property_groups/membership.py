from myvr.api.mixins import ModelViewSet


class Membership(ModelViewSet):
    resource_url = '/property-memberships/'
    model_name = 'Membership'
