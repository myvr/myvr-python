from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Rate
from tests.utils import get_resource_actions, sort_actions


class TestRateResource:
    def test_settings(self):
        assert Rate.resource_url == '/rates/'
        assert Rate.model_name == 'Rate'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Rate)

        assert actual_actions == expected_actions
