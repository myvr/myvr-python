from myvr.api.abstract import CreateMixin, DeleteMixin, ListMixin, UpdateMixin
from myvr.resources import Room


class TestRoomResource:
    def test_settings(self):
        assert Room.resource_url == '/rooms/'
        assert Room.model_name == 'Room'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(Room.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
