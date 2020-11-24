from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Room


class TestRoomResource:
    def test_settings(self):
        assert Room.resource_url == '/rooms/'
        assert Room.model_name == 'Room'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(Room.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
