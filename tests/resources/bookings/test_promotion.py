from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources.bookings.promotion import Promotion
from tests.utils import get_resource_actions, sort_actions


class TestPromotion:
    def test_settings(self):
        assert Promotion.resource_url == '/promotions/'
        assert Promotion.model_name == 'Promotion'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(Promotion)

        assert actual_actions == expected_actions
