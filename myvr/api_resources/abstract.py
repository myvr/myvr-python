import requests
import json

CODE_TO_ERROR = {400: 'BAD_REQUEST', 401: 'UNAUTHORIZED', 402: 'PAYMENT_REQUIRED', 403: 'FORBIDDEN', 404: 'NOT_FOUND',
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


class MyVRObject(dict):
    base_url = ''

    def __init__(self, api_key=None, **kwargs):
        super(MyVRObject, self).__init__()

        self.api_key = api_key
        self.initial_arguments = kwargs
        self.is_error = False

        if not self.api_key:
            raise ValueError('Field: api_key should be specified')

        if not self.base_url:
            raise NotImplementedError('You should specify a base url for given object class')

        if not self.base_url.endswith('/'):
            raise ValueError('The base_url field should ends with "/"')

    @property
    def auth_header(self):
        return {'Authorization': f'Bearer {self.api_key}'}

    def _process_response(self, response):
        self.is_error = not response.ok
        if self.is_error:
            return {'error': CODE_TO_ERROR[response.status_code], 'status_code': response.status_code}

        try:
            response = response.json()
        except json.JSONDecodeError:
            response = response.text

        if response:
            if isinstance(response, dict):
                for key, value in response.items():
                    self[key] = value

            if isinstance(response, list):
                self['response_result'] = response

            if isinstance(response, str):
                self['response_text'] = response

        return self

    def request(self, method, url, headers=None, data=None):
        headers = headers if headers else self.auth_header
        response = requests.request(method, url, headers=headers, data=data)
        return self._process_response(response)


class ApiResource(MyVRObject):

    @classmethod
    def retrieve(cls, key, api_key=None, url=None, **kwargs):
        instance = cls(api_key=api_key, **kwargs)
        url = url if url else cls.base_url + f'{key}/'
        return instance.request('GET', url, data=kwargs)


class CreateMixin(ApiResource):

    @classmethod
    def create(cls, api_key=None, url=None, **kwargs):
        instance = cls(api_key=api_key, **kwargs)
        url = url if url else cls.base_url
        return instance.request('POST', url, data=kwargs)


class UpdateMixin(ApiResource):

    @classmethod
    def put(cls, key, api_key=None, url=None, **kwargs):
        instance = cls(api_key=api_key, **kwargs)
        url = url if url else cls.base_url + f'{key}/'
        return instance.request('PUT', url, data=kwargs)


class DeleteMixin(ApiResource):

    @classmethod
    def delete(cls, key, api_key=None, url=None, **kwargs):
        instance = cls(api_key=api_key, **kwargs)
        url = url if url else cls.base_url + f'{key}/'
        return instance.request('DELETE', url, data=kwargs)


class ListMixin(ApiResource):

    @classmethod
    def list_objects(cls, api_key=None, url=None, **kwargs):
        instance = cls(api_key=api_key, **kwargs)
        url = url if url else cls.base_url
        return instance.request('GET', url, data=kwargs)
