from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Photo
from tests.utils import get_resource_actions, sort_actions


class TestPhotoResource:
    def test_settings(self):
        assert Photo.resource_url == '/photos/'
        assert Photo.model_name == 'Photo'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Photo)

        assert actual_actions == expected_actions
