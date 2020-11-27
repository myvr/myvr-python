from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin


class InquiryMessage(CreateMixin, RetrieveMixin, ListMixin):
    resource_url = '/inquiry-messages/'
    model_name = 'Inquiry Message'
