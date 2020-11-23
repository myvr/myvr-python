class MyVRException(Exception):
    """Wrapper to express our own exception"""
    pass


class MyVRAPIException(Exception):
    """Wrapper to express myvr.com API exception"""

    def __init__(self, data):
        self.data = data
        super(MyVRAPIException, self).__init__()
