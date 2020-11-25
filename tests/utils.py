from typing import Set, Type

from myvr.api.base import APIResource

API_URL = 'http://example.com/'
API_KEY = 'test_api_key'
API_VERSION = 'v1'


def get_common_actions(resource: Type[APIResource], actions: Set[Type[APIResource]]) -> Set[type]:
    return set(resource.__mro__).intersection(actions)
