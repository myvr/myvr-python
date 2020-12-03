from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin


class InquiryMessage(CreateMixin, RetrieveMixin, ListMixin):
    path = 'inquiry-messages'
    name = 'Inquiry Message'
