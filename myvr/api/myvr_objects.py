class MyVRObject(dict):
    """MyVR object wrapper that behaves like dictionary"""

    def __init__(self, fields: dict, name: str = ''):
        """
        :param fields: dict, Dictionary with instance name parameters
        :param name: str. The name of the API instance
        """

        self.name = name
        self.key = fields.get('key', None)
        self.response_text = fields.pop('response_text', None)
        
        super().__init__(fields)


class MyVRCollection(list):
    """MyVR collection wrapper for list method"""

    _meta_params = ['limit', 'offset', 'previous', 'next', 'count']

    def __init__(self, fields: dict, name: str = ''):
        """
        :param fields: dict, Dictionary with instance name parameters
        :param name: str. The name of the API instance
        """

        self.name = name
        self.response_text = fields.pop('response_text', None)
        self.meta = dict({k: v for k, v in fields.items() if k in self._meta_params})

        super().__init__([MyVRObject(i, self.name) for i in fields['results']])
