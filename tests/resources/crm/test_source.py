from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Source
from tests.utils import get_common_actions


class TestSource:
    def test_settings(self):
        assert Source.resource_url == '/sources/'
        assert Source.model_name == 'Source'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin, UpdateMixin, ListMixin}
        actual_actions = get_common_actions(Source, expected_actions)

        assert len(actual_actions) == len(expected_actions)
