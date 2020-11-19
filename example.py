import myvr

api_key = "LIVE_4aa0462404d040fd0237d147cec603be"

prop = myvr.Property.create(api_key=api_key, url='custom_url', **{'name': "API Demo Property"})
print('create', prop)

prop = myvr.Property.retrieve(key=prop.pk, api_key=api_key)
print('retrieve', prop)

prop = myvr.Property.put(key=prop.pk, api_key=api_key, **{'name': 'New API Demo name'})
print('put', prop)

prop = myvr.Property.delete(key=prop.pk, api_key=api_key)
print('delete', prop)

prop = myvr.Property.list_objects(api_key=api_key)
print('list_objects', prop, prop[0].pagination)

prop = myvr.Property.reset_rate(api_key=api_key, key=prop[0].pk,
                                **{'rates': [prop[0]['ratePlan']]})

print('reset_rate', prop, prop.is_error, prop.response_text)

