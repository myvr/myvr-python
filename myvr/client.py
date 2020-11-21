from myvr.resources import Property, Photo
from myvr.api.abstract import ApiResource


class MyVRClient(ApiResource):
    def __init__(self, api_key: str, api_url: str = 'https://api.myvr.com/', version: str = 'v1'):
        super().__init__(api_key, api_url, version)

        self.Property = Property(api_key, api_url, version)
        self.Photo = Photo(api_key, api_url, version)
