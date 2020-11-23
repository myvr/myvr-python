from myvr.api.abstract import CreateMixin, DeleteMixin, ListMixin, UpdateMixin
from myvr.resources import Photo


class TestPhotoResource:
    def test_settings(self):
        assert Photo.resource_url == '/photos/'
        assert Photo.model_name == 'Photo'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(Photo.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
