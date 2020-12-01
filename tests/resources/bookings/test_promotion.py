from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin

from myvr.resources.bookings.promotion import Promotion

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestPromotion:
    def test_settings(self):
        assert Promotion.resource_url == 'promotions'
        assert Promotion.resource_name == 'Promotion'

    def test_base_actions(self):
        expected_actions = sort_actions(
            [CreateMixin, RetrieveMixin, ListMixin]
        )
        actual_actions = get_resource_actions(Promotion)

        assert actual_actions == expected_actions
