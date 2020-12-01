from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin

from myvr.resources import Amenity

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestAmenityResource:
    def test_settings(self):
        assert Amenity.resource_url == 'property-amenities'
        assert Amenity.resource_name == 'Amenity'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin, RetrieveMixin
        ])
        actual_actions = get_resource_actions(Amenity)

        assert actual_actions == expected_actions
