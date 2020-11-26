from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Room
from tests.utils import get_resource_actions, sort_actions


class TestRoomResource:
    def test_settings(self):
        assert Room.resource_url == '/rooms/'
        assert Room.model_name == 'Room'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Room)

        assert actual_actions == expected_actions
