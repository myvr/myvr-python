from functools import partialmethod

from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.api.resource import APIResource


class Reservation(CreateMixin, RetrieveMixin, UpdateMixin, ListMixin):
    path = 'reservations'
    name = 'Reservation'

    create_from_quote = partialmethod(CreateMixin.create)
    update_from_quote = partialmethod(UpdateMixin.update)
    cancel = partialmethod(APIResource.object_action, path='cancel')
    decline = partialmethod(APIResource.object_action, path='decline')
    approve = partialmethod(APIResource.object_action, path='approve')
    assign = partialmethod(APIResource.object_action, path='assign')

    def update(self, key: str, **data) -> MyVRObject:
        url = self.add_path(self.base_url, key)
        return self._client.request(
            'PATCH',
            url,
            self.name,
            data=data
        )
