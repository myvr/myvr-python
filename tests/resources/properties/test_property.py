from myvr.api.abstract import CreateMixin, DeleteMixin, ListMixin, UpdateMixin
from myvr.resources import Property


class TestPropertyResource:
    def test_settings(self):
        assert Property.resource_url == '/properties/'
        assert Property.model_name == 'Property'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(Property.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
