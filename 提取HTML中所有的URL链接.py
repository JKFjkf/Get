from bs4 import  BeautifulSoup
import requests

r = requests.get("https://www.baidu.com")
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo,"lxml")
for link in soup.find_all('a'):
    print(link.get('href'))