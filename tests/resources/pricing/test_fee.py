from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Fee


class TestFeeResource:
    def test_settings(self):
        assert Fee.resource_url == '/fees/'
        assert Fee.model_name == 'Fee'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(Fee.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)
