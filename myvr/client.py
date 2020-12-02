import json
from typing import Union

import requests

from myvr.api.exceptions import MyVRAPIError
from myvr.api.myvr_objects import MyVRCollection
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import Amenity
from myvr.resources import CalendarEvent
from myvr.resources import CancellationReason
from myvr.resources import DailyAvailability
from myvr.resources import Expense
from myvr.resources import Fee
from myvr.resources import Payment
from myvr.resources import PaymentMethod
from myvr.resources import Photo
from myvr.resources import Promotion
from myvr.resources import Property
from myvr.resources import PropertyHierarchy
from myvr.resources import Quote
from myvr.resources import Rate
from myvr.resources import RatePlan
from myvr.resources import Refund
from myvr.resources import Reservation
from myvr.resources import Room


class MyVRClient:
    api_url: str = 'https://api.myvr.com/'

    def __init__(
            self,
            api_key: str,
            version: str = 'v1'
    ):
        self._api_key = api_key
        self._version = version

        # Properties
        self.CalendarEvent = CalendarEvent(self)
        self.DailyAvailability = DailyAvailability(self)
        self.Property = Property(self)
        self.Photo = Photo(self)
        self.Room = Room(self)
        self.Amenity = Amenity(self)
        self.PropertyHierarchy = PropertyHierarchy(self)

        # Bookings
        self.CancellationReason = CancellationReason(self)
        self.Expense = Expense(self)
        self.Quote = Quote(self)
        self.Payment = Payment(self)
        self.PaymentMethod = PaymentMethod(self)
        self.Promotion = Promotion(self)
        self.Refund = Refund(self)
        self.Reservation = Reservation(self)

        # Pricing
        self.Rate = Rate(self)
        self.RatePlan = RatePlan(self)
        self.Fee = Fee(self)
        self.FeePlan = Fee(self)

    @property
    def base_url(self):
        return f'{self.api_url}{self._version}'

    @property
    def auth_header(self) -> dict:
        return {'Authorization': f'Bearer {self._api_key}'}

    def get_headers(self, headers: dict) -> dict:
        if 'Authorization' not in headers:
            headers.update(self.auth_header)

        return headers

    @staticmethod
    def _verify_response(response: requests.Response) -> dict:
        """
        Method to check response on errors and multiple objects containing
        :param response: requests.Response, Response instance
        :return: Dictionary or List with processed values
        """

        try:
            response_data = response.json()
        except json.JSONDecodeError:
            response_data = response.text

        if not response.ok:
            raise MyVRAPIError(
                data={
                    'error': response.reason,
                    'method': response.request.method,
                    'status_code': response.status_code,
                    'message': response_data,
                })

        if isinstance(response_data, str):
            return {'response_text': response_data}

        return response_data

    def request(
            self, 
            method: str, 
            url: str, 
            model_name: str, 
            headers: dict = None, 
            data: dict = None
    ) -> Union[MyVRObject, MyVRCollection]:
        """
        Performs request to the API.
        :param method: str, HTTP method name in uppercase
        :param url: str, The url where to send request
        :param model_name: str, The name of the model
        :param headers: dict, Dictionary with headers, default None
        :param data: dict, Request's body, default None
        :return: MyVRObject with the fields of the model or error information
        """

        headers = self.get_headers(headers if headers else {})
        response = requests.request(method, url, headers=headers, json=data)
        data = self._verify_response(response)
        return self.convert_to_myvr_object(data, model_name)
    
    @staticmethod
    def convert_to_myvr_object(
            response_data: dict, 
            model_name: str
    ) -> Union[MyVRObject, MyVRCollection]:
        
        if isinstance(response_data, list) or 'results' in response_data:
            object_cls = MyVRCollection
        else:
            object_cls = MyVRObject

        return object_cls(response_data, model_name)
