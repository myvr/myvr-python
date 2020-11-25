from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources.bookings.promotion import Promotion
from tests.utils import get_common_actions


class TestPromotion:
    def test_settings(self):
        assert Promotion.resource_url == '/promotions/'
        assert Promotion.model_name == 'Promotion'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(Promotion, expected_actions)

        assert len(actual_actions) == len(expected_actions)
