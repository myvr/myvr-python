![GNU license](https://img.shields.io/badge/licence-GNU-blue.svg)

# MyVR Python Library
***
The MyVR Python library provides access to the MyVR API from 
applications written in Python.

Learn about the MyVR API here:
https://developer.myvr.com/api/

## Getting started
***

### Installation
[comment]: <> (`pip install myvr-python`)

### Initialization

Grab `YOUR_API_KEY` from myvr account (Setup > API & Data Access > API Access). 
Optionally you set api version as `version='v1'` (`'v1'` is default value and only one supported version).

```python
from myvr import MyVRClient

client = MyVRClient(api_key='YOUR_API_KEY')
```

### Pagination

When a list of objects is requested, a paginated result is returned. 
We use a limit/offset pagination approach. Simple add `limit` and `offset` to function call.   
`limit` -  	The maximum number of items to return.  
`offset` - The starting position of the result set in relation to the complete set of unpaginated objects. 

```python
client.Property.list(limit=20, offset=5)
```

List example with query string params:
```python
client.Property.list(
    limit=20,
    offset=5,
    query_params={
        'key': 'value'
    }
)
```

### Responses
Result json response is wrapped into either dict like `MyVRObject` or list like `MyVRCollection`.  
`MyVRObject` stores object's key as meta data and `MyVRCollection` stores pagination info under `meta` key.

`MyVRObject` example:
```python
fee = client.Fee.retrieve('fee_key')
print(type(fee))
# <class 'myvr.api.myvr_objects.MyVRObject'>

print(fee)
# {'key': 'fee_key' ...}

print(fee.key)
# 'fee_key'
```

`MyVRCollection` example:
```python
contacts = client.Contact.list()
print(type(contacts))
# <class 'myvr.api.myvr_objects.MyVRCollection'>

print(contacts.meta)
# {'count': 40, 'limit': 20, 'offset': 0, 'next': 'url', 'previous': None}

print(contacts)
# [
#     {'key': 'obj_key1', ...},
#     {'key': 'obj_key2', ...}, 
#     ...
# ]
```

### Examples

```python
# creates Tag 
client.Tag.create(tag='Test tag')

# updates Property name
client.Property.update('property_key', name='Updated test property')

# deletes Reservation
client.Reservation.delete('reservation_key')

# retrieves Source
client.Source.retrieve('source_key')

# fetches list of Fee records
client.Fee.list()
```

## API structure
***
All endpoints follow the structure listed in the official MyVR documentation. 
The structure will be listed below and then the individual methods available after.

```
MyVR
+- Properties
|  +- Amenity
|  +- Calendar Event
|  +- Daily Availability
|  +- Photo
|  +- Property
|  +- Property Hierarchy
|  +- Room
+- Pricing
|  +- Fee
|  +- Fee Plan
|  +- Rate
|  +- Rate Plan
+- Property Groups
|  +- Group
|  +- Membership
+- Channels
|  +- Channel Listing
+- CRM
|  +- Contact
|  +- Contact Address
|  +- Contact Email
|  +- Contact Note
|  +- Contact Phone
|  +- Contact Tag
|  +- Inquiry
|  +- Inquiry Message
|  +- Message Template
|  +- Source
|  +- Tag
+- Bookings
|  +- Cancellation Reason
|  +- Expense
|  +- Payment
|  +- Payment Method
|  +- Promotion
|  +- Quote
|  +- Refund
|  +- Reservation
+- Settings
|  +- Custom Fields
|  +- Merchant Accounts
+- Accounts
|  +- Account
|  +- User
```

## API endpoints
***
Below is the list of all endpoints and methods that can be called.  
Every endpoint returns `MyVRObject` or `MyVRCollection` for list endpoints.  
Endpoint arguments are passed as `**kwargs` expect of object's key for update, retrieve and delete actions.
For list endpoints you can provide dict with query string params under `query_params` argument name.
The below code assumes that you have initialized the `MyVRClient` class as listed above with the name client.

### Accounts

#### Account
```python
client.Account.retrieve('account_key')
```

#### User
```python
client.User.retrieve('user_key')
client.User.list()
```
