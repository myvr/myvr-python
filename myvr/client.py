from myvr.resources import Property, Photo
from myvr.api.abstract import BaseAPI


class MyVRClient(BaseAPI):
    def __init__(
            self,
            api_key: str,
            api_url: str = 'https://api.myvr.com/',
            version: str = 'v1'
    ):
        super(MyVRClient, self).__init__(api_key, api_url, version)

        self.Property = Property(api_key, api_url, version)
        self.Photo = Photo(api_key, api_url, version)
