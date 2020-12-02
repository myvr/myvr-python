from myvr.api.mixins import ModelViewSet


class ContactEmail(ModelViewSet):
    resource_url = '/contact-emails/'
    model_name = 'Contact Email'
