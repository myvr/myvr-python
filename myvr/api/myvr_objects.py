class MyVRObject(dict):
    """MyVR object wrapper that behaves like dictionary"""

    def __init__(self, fields: dict, name=''):
        """
        :param fields: dict, Dictionary with instance name parameters
        :param name: str. The name of the API instance
        """

        self.name = name

        self.key = fields.get('key', None)
        self.error = fields.get('error', None)
        self.response_text = fields.get('response_text', None)

        if self.response_text:
            fields.pop('response_text')

        super().__init__(fields)


class MyVRCollection(list):

    pagination_params = ['limit', 'offset', 'previous', 'next']

    def __init__(self, fields: dict, name=''):
        self.name = name

        self.error = fields.get('error', None)
        self.response_text = fields.get('response_text', None)

        if self.response_text:
            fields.pop('response_text')

        self.pagination = dict({k: v for k, v in fields.items() if k in self.pagination_params})
        super().__init__([MyVRObject(i, self.name) for i in fields['results']])
