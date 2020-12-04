![GNU license](https://img.shields.io/badge/licence-GNU-blue.svg)

# MyVR Python Library

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

Below is the list of all endpoints and methods that can be called.  
Every endpoint returns `MyVRObject` or `MyVRCollection` for list endpoints.  
Endpoint arguments are passed as `**kwargs` expect of object's key for update, retrieve and delete actions.
For list endpoints you can provide dict with query string params under `query_params` argument name.
The below code assumes that you have initialized the `MyVRClient` class as listed above with the name `client`.

### Accounts

#### Accounts

```python
client.Account.retrieve('account_key')
```

#### Users

```python
client.User.retrieve('user_key')
client.User.list()
```

### CRM

#### Contacts

```python
client.Contact.create(firstName='', lastName='')
client.Contact.retrieve('contact_key')
client.Contact.update('contact_key', firstName='')
client.Contact.list()
```

#### Contact Addresses

```python
client.ContactAddress.create(city='', contact='contact_key')
client.ContactAddress.retrieve('address_key')
client.ContactAddress.update('address_key', city='', contact='contact_key')
client.ContactAddress.list()
client.ContactAddress.delete('address_key')
```

#### Contact Emails

```python
client.ContactEmail.create(email='', contact='contact_key')
client.ContactEmail.retrieve('email_key')
client.ContactEmail.update('email_key', contact='contact_key', type='personal')
client.ContactEmail.list()
client.ContactEmail.delete('email_key')
```

#### Contact Notes

```python
client.ContactNote.create(note='', contact='contact_key')
client.ContactNote.retrieve('note_key')
client.ContactNote.update('note_key', note='', contact='contact_key')
client.ContactNote.list()
client.ContactNote.delete('note_key')
```

#### Contact Phones

```python
client.ContactPhone.create(phone='', contact='contact_key')
client.ContactPhone.retrieve('phone_key')
client.ContactPhone.update('phone_key', contact='contact_key', phone='')
client.ContactPhone.list()
client.ContactPhone.delete('phone_key')
```

#### Contact Tags

```python
client.ContactTag.create(tag='tag_key', contact='contact_key')
client.ContactTag.retrieve('contact_tag_key')
client.ContactTag.update('contact_tag_key', tag='tag_key', contact='contact_key', tag='')
client.ContactTag.list()
client.ContactTag.delete('contact_tag_key')
```

#### Inquiries

```python
client.Inquiry.create(email='', firstName='', lastName='', property='property_key')
client.Inquiry.retrieve('inquiry_key')
client.Inquiry.list()
client.Inquiry.assign('inquiry_key', user='')
```

#### Inquiry Messages

```python
client.InquiryMessage.create(content='', inquiry='inquiry_key')
client.InquiryMessage.retrieve('inquiry_message_key')
client.InquiryMessage.list()
```

#### Message Templates

```python
client.MessageTemplate.retrieve('message_template_key')
client.MessageTemplate.list()
client.MessageTemplate.render('message_template_key')
```

#### Sources

```python
client.Source.create(code='', name='')
client.Source.retrieve('source_key')
client.Source.update('source_key', name='')
client.Source.list()
```

#### Tags

```python
client.Tag.create(tag='')
client.Tag.retrieve('tag_key')
client.Tag.list()
client.Tag.delete('tag_key')
```

### Properties

#### Amenities

```python
client.Amenity.create(amenity='', property='property_key')
client.Amenity.retrieve('amenity_key')
client.Amenity.update(amenity='', property='property_key')
client.Amenity.list()
client.Amenity.delete('amenity_key')
```

#### Calendar Events

```python
client.CalendarEvent.create(property='property_key', startDate='', stopDate='', status='')
client.CalendarEvent.retrieve('calendar_event_key')
client.CalendarEvent.update('calendar_event_key', startDate='')
client.CalendarEvent.list()
client.CalendarEvent.delete('calendar_event_key')
```

#### Daily Availability

```python
client.DailyAvailability.list()
```

#### Photos

```python
client.Photo.create(sourceUrl='', property='property_key')
client.Photo.retrieve('photo_key')
client.Photo.update('photo_key', altText='')
client.Photo.list()
client.Photo.delete('photo_key')
```

#### Property

```python
client.Property.create(name='')
client.Property.retrieve('property_key')
client.Property.update('property_key', name='')
client.Property.list()
client.Property.delete('property_key')
client.Property.reset_rate('property_key')
```

#### Property Hierarchy

```python
client.PropertyHierarchy.list()
```

#### Rooms

```python
client.Room.create(property='property_key')
client.Room.retrieve('room_key')
client.Room.update('room_key')
client.Room.list()
client.Room.delete('room_key')
```
### Pricing

#### Rate Plan
    client.RatePlan.retrieve('RatePlanKey')
    client.RatePlan.list(limit=10, offset=10) or client.RatePlan.list(query_params={'limit': 10, 'offset': 10}) 
    
    client.RatePlan.reset_rate('RatePlanKey')
    
#### Rate
    client.Rate.create(**{'baseRate': True, 'minStay': 3})
    client.Rate.retrieve('RateKey')
    client.Rate.update('RateKey', **{'baseRate': False, 'minStay': 4})
    client.Rate.delete('RateKey')
    client.Rate.list(limit=10, offset=10) or client.Rate.list(query_params={'limit': 10, 'offset': 10}) 

#### Fee Plan
    client.FeePlan.retrieve('FeePlanKey')
    client.FeePlan.list(limit=10, offset=10) or client.FeePlan.list(query_params={'limit': 10, 'offset': 10}) 

#### Fee
    client.Fee.create(**{'cost': 100, 'guestThreshold': 3})
    client.Fee.retrieve('FeeKey')
    client.Fee.update('FeeKey', **{'description': 'new description', 'guestThreshold': 4})
    client.Fee.delete('FeeKey')
    client.Fee.list(limit=10, offset=10) or client.Fee.list(query_params={'limit': 10, 'offset': 10}) 

### Bookings

#### Cancellation Reason
    client.CancellationReason.retrieve('CancellationReasonKey')
    client.CancellationReason.list(limit=10, offset=10) or client.CancellationReason.list(query_params={'limit': 10, 'offset': 10}) 

#### Expense
    client.Expense.retrieve('ExpenseKey')
    client.Expense.list(limit=10, offset=10) or client.Expense.list(query_params={'limit': 10, 'offset': 10}) 

#### Refund
    client.Refund.retrieve('RefundKey')
    client.Refund.list(limit=10, offset=10) or client.Refund.list(query_params={'limit': 10, 'offset': 10}) 

#### Payment
    client.Payment.create(**{'reservation': 'ReservationKey', 'amount': 400'})
    client.Payment.retrieve('PaymentKey')
    client.Payment.list(limit=10, offset=10, **{'status': 'unpaid'}) or client.Payment.list(query_params={'limit': 10, 'offset': 10}) 

    client.Payment.process('PaymentKey', **{'paymentMethod': 'method'})
    client.Payment.refund('PaymentKey', **{'amount': 500})
    client.Payment.record('PaymentKey', **{'datePaid': '2020-02-02'})
    
#### Payment Method
    client.PaymentMethod.create(**{'reservation': 'ReservationKey', 'stripePaymentMethod': 'method'})
    client.PaymentMethod.retrieve('PaymentMethodKey')
    client.PaymentMethod.list(limit=10, offset=10, **{'reservation': 'ReservationKey'}) 

#### Quote
    client.Quote.create(**{'property': 'PropertyKey', 'checkIn': '2020-02-02', 'checkOut': '2020-02-03', 'adults': 2})
    client.Quote.retrieve('QuoteKey')
    
    client.Quote.create_custom(**{'amount': 500, 'checkIn': '2020-02-02', 'checkOut': '2020-02-03'})
    
#### Promotion
    client.Promotion.create(**{'code': 'ASD', 'discounts': [{"cost": "50.000", "currency": "USD"}], 'name': 'name'})
    client.Promotion.retrieve('PromotionKey')
    client.Promotion.list(limit=10, offset=10, **{'reservation': 'ReservationKey'}) 

#### Reservation
    client.Reservation.create(**{**{'property': 'PropertyKey', 'checkIn': '2020-02-02', 'checkOut': '2020-02-03'})
    client.Reservation.retrieve('ReservationKey')
    client.Reservation.update('ReservationKey', **{'adults': 4})
    client.Reservation.list(limit=10, offset=10б **{'status': 'canceled'}) 
    
    client.Reservation.create_from_quote('QuoteKey', **{'validateAvailability': False})
    client.Reservation.update_from_quote('QuoteKey', **{'validateAvailability': True})
    client.Reservation.cancel('ReservationKey')
    client.Reservation.decline('ReservationKey')
    client.Reservation.approve('ReservationKey')

### Property Groups

#### Group
    client.Group.create(**{'name': 'name'})
    client.Group.retrieve('GroupKey')
    client.Group.update('GroupKey', **{'name': 'new name'})
    client.Group.delete('GroupKey')
    client.Group.list(limit=10, offset=10) or client.Group.list(query_params={'limit': 10, 'offset': 10}) 

#### Membership
    client.Membership.create(**{'group': 'GroupKey', 'property': 'PropertyKey'})
    client.Membership.retrieve('MembershipKey')
    client.Membership.update('MembershipKey', **{'property': 'PropertyKey'})
    client.Membership.delete('MembershipKey')
    client.Membership.list(limit=10, offset=10) or client.Membership.list(query_params={'limit': 10, 'offset': 10}) 

### Channel Listing

#### Channel Listing
    client.ChannelListing.retrieve('ChannelListingKey')
    client.ChannelListing.list(limit=10, offset=10) or client.ChannelListing.list(query_params={'limit': 10, 'offset': 10}) 

### Settings

#### Custom Field
    client.CustomField.create(**{'dataType': 'text', 'modelType': 'property'})
    client.CustomField.retrieve('CustomFieldKey')
    client.CustomField.list(limit=10, offset=10) or client.CustomField.list(query_params={'limit': 10, 'offset': 10}) 

#### Merchant Account
    client.MerchantAccount.retrieve('MerchantAccountKey')
    client.MerchantAccount.list(limit=10, offset=10) or client.MerchantAccount.list(query_params={'limit': 10, 'offset': 10}) 
