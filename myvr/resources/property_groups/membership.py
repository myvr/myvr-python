from myvr.api.mixins import ModelViewSet


class Membership(ModelViewSet):
    path = 'property-memberships'
    name = 'Membership'
