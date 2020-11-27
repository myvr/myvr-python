from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin


class Contact(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    resource_url = '/contacts/'
    model_name = 'Contact'

    delete_note = partialmethod(APIResource.object_action, path='delete-note/')
    delete_phone = partialmethod(APIResource.object_action, path='delete-phone/')
    delete_tag = partialmethod(APIResource.object_action, path='delete-tag/')
    delete_email = partialmethod(APIResource.object_action, path='delete-email/')
