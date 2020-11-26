from myvr.api.mixins import CreateMixin, ListMixin, RetrieveMixin
from myvr.resources import InquiryMessage
from tests.utils import get_common_actions


class TestInquiryMessage:
    def test_settings(self):
        assert InquiryMessage.resource_url == '/inquiry-messages/'
        assert InquiryMessage.model_name == 'Inquiry Message'

    def test_base_actions(self):
        expected_actions = {CreateMixin, RetrieveMixin, ListMixin}
        actual_actions = get_common_actions(InquiryMessage, expected_actions)

        assert len(actual_actions) == len(expected_actions)
