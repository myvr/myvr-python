from myvr.api.mixins import CreateMixin
from myvr.api.mixins import ListMixin
from myvr.api.mixins import RetrieveMixin
from myvr.resources import InquiryMessage
from tests.utils import get_resource_actions
from tests.utils import sort_actions


class TestInquiryMessage:
    def test_settings(self):
        assert InquiryMessage.path == 'inquiry-messages'
        assert InquiryMessage.name == 'Inquiry Message'

    def test_base_actions(self):
        expected_actions = sort_actions([CreateMixin, RetrieveMixin, ListMixin])
        actual_actions = get_resource_actions(InquiryMessage)

        assert actual_actions == expected_actions
