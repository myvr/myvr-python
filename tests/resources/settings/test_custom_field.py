from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources import CustomField
from tests.utils import get_resource_actions, sort_actions


class TestCustomFieldResource:
    def test_settings(self):
        assert CustomField.resource_url == '/custom-fields/'
        assert CustomField.model_name == 'Custom Field'

    def test_base_actions(self):
        expected_actions = sort_actions([
            CreateMixin, RetrieveMixin, ListMixin
        ])

        actual_actions = get_resource_actions(CustomField)

        assert actual_actions == expected_actions
