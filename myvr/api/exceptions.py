class MyVRException(Exception):
    """Wrapper to express our own exception"""
    pass


class ResourceUrlError(MyVRException):
    def __str__(self):
        return 'API url must end with /'
