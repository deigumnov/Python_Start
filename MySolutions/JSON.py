import ssl
import urllib.request
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1051396.json'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)

print(sum(int(i["count"]) for i in info["comments"]))
