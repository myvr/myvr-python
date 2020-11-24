from myvr.api.mixins import ListMixin
from myvr.resources import PropertyHierarchy


class TestPropertyHierarchyResource:
    def test_settings(self):
        assert PropertyHierarchy.resource_url == '/property-hierarchy/'
        assert PropertyHierarchy.model_name == 'Property Hierarchy'

    def test_base_actions(self):
        expected_actions = {ListMixin}
        actual_actions = set(PropertyHierarchy.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
