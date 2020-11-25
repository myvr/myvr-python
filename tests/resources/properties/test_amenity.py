from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Amenity
from tests.utils import get_common_actions


class TestAmenityResource:
    def test_settings(self):
        assert Amenity.resource_url == '/property-amenities/'
        assert Amenity.model_name == 'Amenity'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        }
        actual_actions = get_common_actions(Amenity, expected_actions)

        assert len(actual_actions) == len(expected_actions)
