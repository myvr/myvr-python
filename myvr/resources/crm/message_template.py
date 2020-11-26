from functools import partialmethod

from myvr.api.base import APIResource
from myvr.api.mixins import ListMixin, RetrieveMixin


class MessageTemplate(RetrieveMixin, ListMixin):
    resource_url = '/message-templates/'
    model_name = 'Message Template'

    render = partialmethod(APIResource.object_action, path='render/')
