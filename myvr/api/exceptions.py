__all__ = [
    'MyVRError',
    'ResourceUrlError',
    'MyVRAPIError',
]


class MyVRError(Exception):
    """Wrapper to express our own exception"""
    pass


class ResourceUrlError(MyVRError):
    def __str__(self):
        return 'API url should not contain /'


class MyVRAPIError(Exception):
    """Wrapper to express myvr.com API exception"""

    def __init__(self, data):
        self.data = data
        super(MyVRAPIError, self).__init__()
