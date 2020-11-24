from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin


class Photo(CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/photos/'
    model_name = 'Photo'
