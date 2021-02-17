import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://guba.sina.com.cn/?s=bar&name=sh000001'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

mydivs = soup.find_all("div", class_="author")

index = 0
for div in mydivs:
    print(index, '', end='')
    for item in div:
        print(item.get_text(), end=' ')
    print()
    index += 1
