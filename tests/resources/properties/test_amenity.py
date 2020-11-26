from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Amenity
from tests.utils import get_resource_actions, sort_actions


class TestAmenityResource:
    def test_settings(self):
        assert Amenity.resource_url == '/property-amenities/'
        assert Amenity.model_name == 'Amenity'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        ])
        actual_actions = get_resource_actions(Amenity)

        assert actual_actions == expected_actions
