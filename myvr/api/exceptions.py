__all__ = [
    'MyVRException',
    'ResourceUrlError',
    'MyVRAPIException',
]


class MyVRException(Exception):
    """Wrapper to express our own exception"""
    pass


class ResourceUrlError(MyVRException):
    def __str__(self):
        return 'API url must end with /'


class MyVRAPIException(Exception):
    """Wrapper to express myvr.com API exception"""

    def __init__(self, data):
        self.data = data
        super(MyVRAPIException, self).__init__()
