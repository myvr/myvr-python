from myvr.api.base import BaseAPI
from myvr.resources import (
    Amenity,
    CalendarEvent,
    CancellationReason,
    Contact,
    ContactAddress,
    ContactTag,
    DailyAvailability,
    Expense,
    Fee,
    Inquiry,
    InquiryMessage,
    MessageTemplate,
    Payment,
    PaymentMethod,
    Photo,
    Promotion,
    Property,
    PropertyHierarchy,
    Quote,
    Rate,
    Refund,
    Reservation,
    Room,
    Source,
    Tag,
)


class MyVRClient(BaseAPI):
    def __init__(
            self,
            api_key: str,
            api_url: str = 'https://api.myvr.com/',
            version: str = 'v1'
    ):
        super(MyVRClient, self).__init__(api_key, api_url, version)

        # Properties
        self.CalendarEvent = CalendarEvent(api_key, api_url, version)
        self.DailyAvailability = DailyAvailability(api_key, api_url, version)
        self.Property = Property(api_key, api_url, version)
        self.Photo = Photo(api_key, api_url, version)
        self.Room = Room(api_key, api_url, version)
        self.Amenity = Amenity(api_key, api_url, version)
        self.PropertyHierarchy = PropertyHierarchy(api_key, api_url, version)

        # Bookings
        self.CancellationReason = CancellationReason(api_key, api_url, version)
        self.Expense = Expense(api_key, api_url, version)
        self.Quote = Quote(api_key, api_url, version)
        self.Payment = Payment(api_key, api_url, version)
        self.PaymentMethod = PaymentMethod(api_key, api_url, version)
        self.Promotion = Promotion(api_key, api_url, version)
        self.Refund = Refund(api_key, api_url, version)
        self.Reservation = Reservation(api_key, api_url, version)

        # Pricing
        self.Rate = Rate(api_key, api_url, version)
        self.Fee = Fee(api_key, api_url, version)
        self.FeePlan = Fee(api_key, api_url, version)

        # CRM
        self.Contact = Contact(api_key, api_url, version)
        self.ContactAddress = ContactAddress(api_key, api_url, version)
        self.ContactTag = ContactTag(api_key, api_url, version)
        self.Inquiry = Inquiry(api_key, api_url, version)
        self.InquiryMessage = InquiryMessage(api_key, api_url, version)
        self.MessageTemplate = MessageTemplate(api_key, api_url, version)
        self.Source = Source(api_key, api_url, version)
        self.Tag = Tag(api_key, api_url, version)
