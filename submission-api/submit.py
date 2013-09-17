import urllib
import urllib2

BASE_URL = 'http://127.0.0.1:8000/main/add/quantity'


def add_quantity(name, object, value, unit, user, uncertainty=None, origin=None):

    # Required arguments

    values = {
        'name': name,
        'object': object,
        'value': value,
        'unit': unit,
        'user': user
    }

    if uncertainty is not None:
        values['uncertainty'] = uncertainty

    if origin is not None:
        values['origin'] = origin

    # Encode the POST request
    data = urllib.urlencode(values)

    # Prepare request
    req = urllib2.Request(BASE_URL, data)

    # Send request
    print(req)
    response = urllib2.urlopen(req)

    print(response.read())

add_quantity('flux', '51pegb', 1.2, 'mJy', 'tom')

# http://127.0.0.1:8000/main/add_quantity/?a=1
