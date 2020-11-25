from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Rate
from tests.utils import get_common_actions


class TestRateResource:
    def test_settings(self):
        assert Rate.resource_url == '/rates/'
        assert Rate.model_name == 'Rate'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = get_common_actions(Rate, expected_actions)

        assert len(actual_actions) == len(expected_actions)
