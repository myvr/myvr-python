from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin

from myvr.resources import Photo

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestPhotoResource:
    def test_settings(self):
        assert Photo.path == 'photos'
        assert Photo.name == 'Photo'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Photo)

        assert actual_actions == expected_actions
