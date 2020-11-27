from myvr.api.mixins import ListMixin, RetrieveMixin
from myvr.resources import MerchantAccount
from tests.utils import get_resource_actions, sort_actions


class TestMerchantAccountResource:
    def test_settings(self):
        assert MerchantAccount.resource_url == '/merchant-accounts/'
        assert MerchantAccount.model_name == 'Merchant Account'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(MerchantAccount)

        assert actual_actions == expected_actions
