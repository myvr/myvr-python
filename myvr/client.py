from myvr.api.base import BaseAPI
from myvr.resources import (
    Amenity,
    CalendarEvent,
    DailyAvailability,
    PaymentMethod,
    Photo,
    Property,
    PropertyHierarchy,
    Quote,
    Rate,
    Reservation,
    Room,
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
        self.Quote = Quote(api_key, api_url, version)
        self.PaymentMethod = PaymentMethod(api_key, api_url, version)
        self.Reservation = Reservation(api_key, api_url, version)

        # Pricing
        self.Rate = Rate(api_key, api_url, version)
