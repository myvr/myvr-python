from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Photo
from tests.utils import get_common_actions


class TestPhotoResource:
    def test_settings(self):
        assert Photo.resource_url == '/photos/'
        assert Photo.model_name == 'Photo'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = get_common_actions(Photo, expected_actions)

        assert len(actual_actions) == len(expected_actions)
