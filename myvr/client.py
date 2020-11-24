from myvr.api.base import BaseAPI
from myvr.resources import CalendarEvent, DailyAvailability, Photo, Property, Room


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
