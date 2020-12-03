from myvr.api.mixins import ListMixin
from myvr.resources import PropertyHierarchy
from tests.utils import get_resource_actions


class TestPropertyHierarchyResource:
    def test_settings(self):
        assert PropertyHierarchy.path == 'property-hierarchy'
        assert PropertyHierarchy.name == 'Property Hierarchy'

    def test_base_actions(self):
        actual_actions = get_resource_actions(PropertyHierarchy)
        assert actual_actions == [ListMixin]
