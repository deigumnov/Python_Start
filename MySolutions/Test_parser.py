import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter URL: ')
# count = int(input('Enter count: '))
# pos = int(input('Enter position: '))
url = 'http://py4e-data.dr-chuck.net/known_by_Albert.html'
count = 7
pos = 18

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    index = 0
    for tag in tags:
        index += 1
        if index == pos:
            if i == count - 1:
                print(tag.contents[0])
            else:
                url = 'http://py4e-data.dr-chuck.net/known_by_' + tag.contents[0] + '.html'
            break
