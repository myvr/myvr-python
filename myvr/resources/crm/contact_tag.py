from myvr.api.mixins import ModelViewSet


class ContactTag(ModelViewSet):
    resource_url = '/contact-tags/'
    model_name = 'Contact Tag'
