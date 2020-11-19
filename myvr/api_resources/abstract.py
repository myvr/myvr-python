import requests
import json

CODE_TO_MSG = {400: 'BAD_REQUEST', 401: 'UNAUTHORIZED', 402: 'PAYMENT_REQUIRED', 403: 'FORBIDDEN', 404: 'NOT_FOUND',
               405: 'METHOD_NOT_ALLOWED', 406: 'NOT_ACCEPTABLE', 407: 'PROXY_AUTHENTICATION_REQUIRED',
               408: 'REQUEST_TIMEOUT', 409: 'CONFLICT', 410: 'GONE', 411: 'LENGTH_REQUIRED',
               412: 'PRECONDITION_FAILED', 413: 'REQUEST_ENTITY_TOO_LARGE', 414: 'REQUEST_URI_TOO_LONG',
               415: 'UNSUPPORTED_MEDIA_TYPE', 416: 'REQUESTED_RANGE_NOT_SATISFIABLE', 417: 'EXPECTATION_FAILED',
               418: 'IM_A_TEAPOT', 422: 'UNPROCESSABLE_ENTITY', 423: 'LOCKED', 424: 'FAILED_DEPENDENCY',
               426: 'UPGRADE_REQUIRED', 428: 'PRECONDITION_REQUIRED', 429: 'TOO_MANY_REQUESTS',
               431: 'REQUEST_HEADER_FIELDS_TOO_LARGE', 451: 'UNAVAILABLE_FOR_LEGAL_REASONS',
               500: 'INTERNAL_SERVER_ERROR', 501: 'NOT_IMPLEMENTED', 502: 'BAD_GATEWAY', 503: 'SERVICE_UNAVAILABLE',
               504: 'GATEWAY_TIMEOUT', 505: 'HTTP_VERSION_NOT_SUPPORTED', 506: 'VARIANT_ALSO_NEGOTIATES',
               507: 'INSUFFICIENT_STORAGE', 508: 'LOOP_DETECTED', 509: 'BANDWIDTH_LIMIT_EXCEEDED',
               510: 'NOT_EXTENDED', 511: 'NETWORK_AUTHENTICATION_REQUIRED'}


class MyVRException(Exception):
    """Wrapper to express our own exception"""
    pass


class MyVRObject(dict):
    """MyVR object wrapper that behaves like dictionary"""

    def __init__(self, fields: dict, name=''):
        """
        :param fields: dict, Dictionary with instance name parameters
        :param name: str. The name of the API instance
        """
        self.name = name
        self.pagination = fields.get('pagination', None)
        self.response_text = fields.get('response_text', None)

        if 'pagination' in fields:
            fields.pop('pagination')

        if 'response_text' in fields:
            fields.pop('response_text')

        super(MyVRObject, self).__init__(**fields)

    @property
    def is_error(self):
        return self.get('error', None) is not None

    @property
    def pk(self):
        """Returns key field of the object or None for native usability"""
        return self.get('key', None)


class ApiResource:
    """
    ApiResource abstract class that performs API calls and response processing.
    base_url: str, API-url to perform requests should be specified in general class not the abstract.
    model_name: str, The name of the model should be specified in general class not the abstract.
    """

    base_url, model_name = '', ''
    pagination_params = ['limit', 'offset', 'previous', 'next']

    def __init__(self, api_key=''):
        """:param api_key: str, API key from MyVR.com """

        self.api_key = api_key

        if not self.api_key:
            raise MyVRException('Field: api_key should be specified')

        if not self.base_url:
            raise MyVRException('You should specify a base url for given object class')

        if not self.base_url.endswith('/'):
            raise MyVRException('The base_url field should end with "/"')

    @property
    def auth_header(self):
        """Returns auth header"""
        return {'Authorization': f'Bearer {self.api_key}'}

    def _verify_response(self, response: requests.Response, many):
        """
        Method to check response on errors and multiple objects containing
        :param response: requests.Response, Response instance
        :return: Dictionary or List with processed values
        """

        result = [] if many else {}
        if not response.ok:
            result = {'error': CODE_TO_MSG[response.status_code], 'status_code': response.status_code}

        try:
            response = response.json()
        except json.JSONDecodeError:
            response = response.text
            result['response_text'] = response
            return result

        if not isinstance(response, dict):
            raise TypeError(f'Response should be a dictionary. Given: {type(response)}')

        if response:
            if many:
                if 'results' not in response:
                    raise ValueError('many parameter was specified but response has no results field')

                pagination = dict({k: v for k, v in response.items() if k in self.pagination_params})
                for res in response['results']:
                    res['pagination'] = pagination
                    result.append(res)
            else:
                for key, value in response.items():
                    result[key] = value

        return result

    def request(self, method: str, url: str, headers=None, data=None, many=False):
        """
        Performs request to the API.
        :param method: str, HTTP method name in uppercase
        :param url: str, The url where to send request
        :param headers: dict, Dictionary with headers, default None
        :param data: dict, Request's body, default None
        :param many: bool, The flag that defines whether to return many objects or only one instance
        :return: MyVRObject with the fields of the model or error information
        """

        headers = headers if headers else self.auth_header
        response = requests.request(method, url, headers=headers, data=data)
        objects = self._verify_response(response, many)

        return [MyVRObject(i, self.model_name) for i in objects] if many else MyVRObject(objects, self.model_name)

    @classmethod
    def retrieve(cls, key: str, api_key=None, **data):
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param api_key: str, API key from MyVR.com, default None
        :param url: str, The url where to send request, default None
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        instance = cls(api_key=api_key)
        return instance.request('GET', cls.base_url + f'{key}/', data=data)


class CreateMixin(ApiResource):

    @classmethod
    def create(cls, api_key='', **data):
        """
        Base method to perform POST request
        :param api_key: str, API key from MyVR.com, default None
        :param url: str, The url where to send request, default None
        :param data: dict, Request's body, default None
        :return: Created MyVRObject instance or error information
        """

        instance = cls(api_key=api_key)
        return instance.request('POST', cls.base_url, data=data)


class UpdateMixin(ApiResource):

    @classmethod
    def put(cls, key, api_key='', **data):
        """
        Base method to perform PUT request
        :param key: str, The primary key of the instance
        :param api_key: str, API key from MyVR.com, default None
        :param url: str, The url where to send request, default None
        :param data: dict, Request's body, default None
        :return: MyVRObject instance with given key or error information
        """

        instance = cls(api_key=api_key)
        return instance.request('PUT', cls.base_url + f'{key}/', data=data)


class DeleteMixin(ApiResource):

    @classmethod
    def delete(cls, key, api_key='', **data):
        """
        Base method to perform GET request
        :param key: str, The primary key of the instance
        :param api_key: str, API key from MyVR.com, default None
        :param url: str, The url where to send request, default None
        :param data: dict, Request's body, default None
        :return: Empty MyVRObject instance or error information
        """

        instance = cls(api_key=api_key)
        return instance.request('DELETE', cls.base_url + f'{key}/', data=data)


class ListMixin(ApiResource):

    @classmethod
    def list_objects(cls, api_key='', limit=0, offset=0, **data):
        """
        Base method to perform GET request for many data points
        :param api_key: str, API key from MyVR.com, default None
        :param url: str, The url where to send request, default None
        :param limit: int, Pagination parameter. The limit of the query, default 0
        :param offset: int, Pagination parameter. The offset of the query, default 0
        :param data: dict, Request's body, default None
        :return: List of MyVRObject instances or error information
        """

        instance = cls(api_key=api_key)

        if limit not in data:
            data['limit'] = limit

        if offset not in data:
            data['offset'] = offset

        return instance.request('GET', cls.base_url, data=data, many=True)
