# shift +control+ I
# Network
# API search
# if not:
#
import requests
from lxml import html

url='https://novini.bg/'
response=requests.get(url)
tree=html.fromstring(response.text)
# inspect, hover, select, right click, copy xpath 2:10
elements=tree.xpath('/html/body/main/section[2]/div/section[2]/article[4]/a/h2')


for e in elements:
    print(e.text)