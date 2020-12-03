from myvr.api.mixins import CreateMixin
from myvr.api.mixins import DeleteMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin

from myvr.resources import Rate

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestRateResource:
    def test_settings(self):
        assert Rate.path == 'rates'
        assert Rate.name == 'Rate'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Rate)

        assert actual_actions == expected_actions
