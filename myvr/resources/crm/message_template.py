from functools import partialmethod

from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.resource import APIResource


class MessageTemplate(RetrieveMixin, ListMixin):
    path = 'message-templates'
    name = 'Message Template'

    render = partialmethod(APIResource.object_action, path='render')
