from myvr import MyVRAPIException, MyVRClient
from myvr.api.mixins import CreateMixin, DeleteMixin, ListMixin, RetrieveMixin, UpdateMixin
from myvr.api.myvr_objects import MyVRObject
from myvr.resources import Property


class TestPropertyResource:
    def test_settings(self):
        assert Property.resource_url == '/properties/'
        assert Property.model_name == 'Property'

    def test_base_actions(self):
        expected_actions = {
            CreateMixin, RetrieveMixin, UpdateMixin, DeleteMixin, ListMixin
        }
        actual_actions = set(Property.__mro__).intersection(expected_actions)

        assert len(actual_actions) == len(expected_actions)


class TestResetRateMethod:

    def test_invalid_body(self, api_key, api_url, key, version):
        error_msg = {'error': 'Bad Request', 'method': 'PUT', 'status_code': 400,
                     'message': {'non_field_errors': ['Expected a list of items but got type "dict".']}}

        client = MyVRClient(api_key=api_key, api_url=api_url, version=version)
        prop = client.Property.create(**{'name': "API Demo Property"})

        try:
            res = client.Property.reset_rate(key, **{})
        except MyVRAPIException as e:
            assert error_msg == e.data

        client.Property.delete(prop.key)

    def test_correct_body(self, api_key, api_url, version):
        expected_response = {}
        client = MyVRClient(api_key=api_key, api_url=api_url, version=version)
        prop = client.Property.create(**{'name': "API Demo Property"})
        res = Property.reset_rate(prop.key, **{'rates': [prop['ratePlan']]})

        assert isinstance(res, MyVRObject)
        assert res == expected_response

        client.Property.delete(prop.key)


