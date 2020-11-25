from myvr.api.mixins import ListMixin
from myvr.resources import PropertyHierarchy
from tests.utils import get_common_actions


class TestPropertyHierarchyResource:
    def test_settings(self):
        assert PropertyHierarchy.resource_url == '/property-hierarchy/'
        assert PropertyHierarchy.model_name == 'Property Hierarchy'

    def test_base_actions(self):
        expected_actions = {ListMixin}
        actual_actions = get_common_actions(PropertyHierarchy, expected_actions)

        assert len(actual_actions) == len(expected_actions)
