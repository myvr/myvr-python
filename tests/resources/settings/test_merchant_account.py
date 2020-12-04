from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin

from myvr.resources import MerchantAccount

from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestMerchantAccountResource:
    def test_settings(self):
        assert MerchantAccount.path == 'merchant-accounts'
        assert MerchantAccount.name == 'Merchant Account'

    def test_base_actions(self):
        expected_actions = sort_actions([RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(MerchantAccount)

        assert actual_actions == expected_actions
