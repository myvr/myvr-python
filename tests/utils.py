from typing import Set, Type, TypeVar

from myvr.api.base import APIResource

API_URL = 'http://example.com/'
API_KEY = 'test_api_key'
API_VERSION = 'v1'

API_SOURCE_URL = f'{API_URL}{API_VERSION}'
RESOURCE_PARAMS = (API_KEY, API_URL, API_VERSION)


def get_common_actions(resource: Type[APIResource], actions: Set[Type[APIResource]]) -> Set[type]:
    return set(resource.__mro__).intersection(actions)


ResourceType = TypeVar('ResourceType', bound=APIResource)


def init_resource(resource: Type[APIResource], *args) -> ResourceType:
    params = RESOURCE_PARAMS
    if args:
        params = args

    return resource(*params)
