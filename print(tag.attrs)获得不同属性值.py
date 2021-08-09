import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.baidu.com/')
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
tag = soup.a
print(tag.attrs)
print(tag.attrs['class'])
print(tag)