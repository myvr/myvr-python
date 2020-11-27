from myvr.api.mixins import CreateMixin, RetrieveMixin, ListMixin


class CustomField(CreateMixin, RetrieveMixin, ListMixin):
    resource_url = '/custom-fields/'
    model_name = 'Custom Field'
