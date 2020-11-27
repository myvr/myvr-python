from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.resources import Source
from tests.utils import get_resource_actions, sort_actions


class TestSource:
    def test_settings(self):
        assert Source.resource_url == '/sources/'
        assert Source.model_name == 'Source'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, UpdateMixin, ListMixin])
        actual_actions = get_resource_actions(Source)

        assert actual_actions == expected_actions
