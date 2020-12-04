from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.api.mixins import UpdateMixin
from myvr.resources import Source
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestSource:
    def test_settings(self):
        assert Source.path == 'sources'
        assert Source.name == 'Source'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, UpdateMixin, ListMixin])
        actual_actions = get_resource_actions(Source)

        assert actual_actions == expected_actions
