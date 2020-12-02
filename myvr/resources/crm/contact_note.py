from myvr.api.mixins import ModelViewSet


class ContactNote(ModelViewSet):
    resource_url = '/contact-notes/'
    model_name = 'Contact Note'
