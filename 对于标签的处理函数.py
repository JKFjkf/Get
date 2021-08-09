import requests
from bs4 import BeautifulSoup

r=requests.get("https://book.douban.com/latest")
demo = r.text
soup = BeautifulSoup(demo,"lxml")
tag = soup.tbody
print(tag)
print(len(tag.contents))
print(tag.contents[1])
for child in tag.children:
    print(child)
