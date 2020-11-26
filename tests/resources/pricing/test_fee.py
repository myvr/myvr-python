from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Fee
from tests.utils import get_resource_actions, sort_actions


class TestFeeResource:
    def test_settings(self):
        assert Fee.resource_url == '/fees/'
        assert Fee.model_name == 'Fee'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        ])
        actual_actions = get_resource_actions(Fee)

        assert actual_actions == expected_actions
