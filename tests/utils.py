from typing import List
from typing import Type
from typing import TypeVar

from myvr import MyVRClient
from myvr.api.mixins import ModelViewSet
from myvr.api.resource import APIResource

API_URL = 'http://example.com/'
API_KEY = 'test_api_key'
API_VERSION = 'v1'

API_SOURCE_URL = f'{API_URL}{API_VERSION}'
RESOURCE_PARAMS = (API_KEY, API_URL, API_VERSION)

ResourceClass = Type[APIResource]
ResourceInstance = TypeVar('ResourceInstance', bound=APIResource)


class MockClient(MyVRClient):
    api_url = API_URL


def create_client() -> MockClient:
    return MockClient(API_KEY, API_VERSION)


def get_resource_actions(resource: ResourceClass) -> List[ResourceClass]:
    exclude = [APIResource, resource, ModelViewSet]
    actions = [
        cls for cls in resource.__mro__
        if issubclass(cls, APIResource) and cls not in exclude
    ]
    return sort_actions(actions)


def init_resource(resource: ResourceClass, *args) -> ResourceInstance:
    params = RESOURCE_PARAMS
    if args:
        params = args

    return resource(*params)


def sort_actions(actions: List[ResourceClass]) -> List[ResourceClass]:
    return sorted(actions, key=lambda r: r.__name__)
