import myvr

api_key = "LIVE_4aa0462404d040fd0237d147cec603be"

prop = myvr.Property.create(api_key=api_key, **{'name': "API Demo Property"})
print(type(prop), prop)

prop = myvr.Property.retrieve(key=prop['key'], api_key=api_key)
print(type(prop), prop)

prop = myvr.Property.put(key=prop['key'], api_key=api_key, **{'name': 'New API Demo name'})
print(type(prop), prop)

prop = myvr.Property.delete(key=prop['key'], api_key=api_key)
print(type(prop), prop)

prop = myvr.Property.list_objects(api_key=api_key)
print(type(prop), prop)

prop = myvr.Property.reset_rate(api_key=api_key, key=prop['results'][0]['key'],
                                **{'rates': [prop['results'][0]['ratePlan']]})
print(type(prop), prop)
