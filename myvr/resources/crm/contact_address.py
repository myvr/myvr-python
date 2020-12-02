from myvr.api.mixins import ModelViewSet


class ContactAddress(ModelViewSet):
    resource_url = '/contact-addresses/'
    model_name = 'Contact Address'
