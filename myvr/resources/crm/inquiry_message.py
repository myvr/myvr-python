from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin


class InquiryMessage(CreateMixin, RetrieveMixin, ListMixin):
    path = 'inquiry-messages'
    name = 'Inquiry Message'
