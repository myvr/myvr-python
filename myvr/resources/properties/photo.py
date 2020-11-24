from myvr.api.abstract import ListMixin, CreateMixin, UpdateMixin, DeleteMixin


class Photo(CreateMixin, UpdateMixin, DeleteMixin, ListMixin):
    resource_url = '/photos/'
    model_name = 'Photo'
