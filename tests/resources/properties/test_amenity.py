from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, UpdateMixin, RetrieveMixin
from myvr.resources import Amenity


class TestAmenityResource:
    def test_settings(self):
        assert Amenity.resource_url == '/property-amenities/'
        assert Amenity.model_name == 'Amenity'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        }
        actual_actions = set(Amenity.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
