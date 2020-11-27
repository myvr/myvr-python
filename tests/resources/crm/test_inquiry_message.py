from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources import InquiryMessage
from tests.utils import get_resource_actions, sort_actions


class TestInquiryMessage:
    def test_settings(self):
        assert InquiryMessage.resource_url == '/inquiry-messages/'
        assert InquiryMessage.model_name == 'Inquiry Message'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(InquiryMessage)

        assert actual_actions == expected_actions
