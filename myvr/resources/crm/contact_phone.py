from myvr.api.mixins import ModelViewSet


class ContactPhone(ModelViewSet):
    resource_url = '/contact-phones/'
    model_name = 'Contact Phone'
