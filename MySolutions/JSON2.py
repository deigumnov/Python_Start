import ssl
import urllib.parse
import urllib.request
import json

api_key = False

if not api_key:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# address = input('Enter location: ')
address = 'Virginia Commonwealth University'

params = {'address': address}
if api_key:
    params['key'] = api_key

url = service_url + urllib.parse.urlencode(params)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

place_id = js['results'][0]['place_id']
print(place_id)
