from typing import Union


class MyVRObject(dict):
    """MyVR object wrapper that behaves like dictionary"""

    def __init__(self, fields: dict, name: str):
        """
        :param fields: dict, Dictionary with instance name parameters
        :param name: str. The name of the API instance.
        """

        self.name = name
        self.key = fields.get('key')
        self.response_text = fields.pop('response_text', None)

        super().__init__(fields)


class MyVRCollection(list):
    """MyVR collection wrapper for list method"""

    _meta_params = ['limit', 'offset', 'previous', 'next', 'count']

    def __init__(self, data: Union[dict, list], name: str):
        """
        :param data: dict, Dictionary with instance name parameters
        :param name: str. The name of the API instance.
        """

        self.name = name
        self.response_text = None
        self.meta = {}

        if isinstance(data, dict):
            self.response_text = data.pop('response_text', None)
            self.meta = dict({
                k: v for k, v in data.items() if k in self._meta_params
            })
            records = data['results']
        else:
            records = data

        super().__init__([MyVRObject(r, self.name) for r in records])
