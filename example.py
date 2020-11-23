import myvr

client = myvr.MyVRClient(api_key="LIVE_4aa0462404d040fd0237d147cec603be", api_url='https://api.myvr.com/')

try:
    prop = client.Property.create() #**{'name': "API Demo Property"})
    print('create', prop)

    prop = client.Property.retrieve(key=prop.key)
    print('retrieve', prop)

    prop = client.Property.put(key=prop.key, **{'name': 'New API Demo name'})
    print('put', prop)

    prop = client.Property.delete(key=prop.key)
    print('delete', 'error:', prop.error)

except myvr.MyVRAPIException as e:
    print(e.data)

prop = client.Property.list()
print('list', type(prop), prop.pagination, type(prop[0]))

prop = client.Property.reset_rate(prop[0].key, **{'rates': [prop[0]['ratePlan']]})
print('reset_rate', prop, prop.error)

